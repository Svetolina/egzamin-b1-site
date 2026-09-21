#!/usr/bin/env python3
"""Резка записи экзамена по заданиям.

Два режима:
  python tools/split_audio.py silences запись.mp3
      печатает паузы длиннее 8 секунд: по ним видно структуру записи
      (объявление задания, пауза на чтение, первое прослушивание, пауза, второе).
  python tools/split_audio.py cut запись.mp3 audio/<id-теста> cuts.json
      режет запись по границам из cuts.json и кодирует каждый кусок в m4a.

cuts.json: {"s1": [0, 260], "s2": [263, 543], ...}  (секунды: начало, конец)
Нужен ffmpeg в PATH.
"""
import json, re, subprocess, sys, os

def silences(path, min_d=8, noise='-38dB'):
    p = subprocess.run(['ffmpeg', '-hide_banner', '-i', path, '-af',
                        f'silencedetect=noise={noise}:d={min_d}', '-f', 'null', '-'],
                       capture_output=True, text=True)
    start = None
    for line in p.stderr.replace('\r', '\n').splitlines():
        m = re.search(r'silence_(start|end): ([\d.]+)', line)
        if not m:
            continue
        if m.group(1) == 'start':
            start = float(m.group(2))
        elif start is not None:
            end = float(m.group(2))
            print(f'{start:8.1f} - {end:8.1f}  ({end - start:5.1f} s)')
            start = None

def cut(path, out_dir, cuts_file):
    os.makedirs(out_dir, exist_ok=True)
    cuts = json.load(open(cuts_file, encoding='utf8'))
    for name, (a, b) in cuts.items():
        out = os.path.join(out_dir, f'{name}.m4a')
        subprocess.run(['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error',
                        '-ss', str(a), '-i', path, '-t', str(round(b - a, 2)),
                        '-vn', '-ac', '1', '-ar', '32000', '-c:a', 'aac', '-b:a', '40k',
                        '-movflags', '+faststart', out], check=True)
        print('ok', out)

if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'silences':
        silences(sys.argv[2])
    elif len(sys.argv) == 5 and sys.argv[1] == 'cut':
        cut(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(__doc__)
