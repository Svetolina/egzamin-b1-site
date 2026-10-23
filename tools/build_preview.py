#!/usr/bin/env python3
"""Собирает страницу-предпросмотр темы учебника из topic.json + extract.json.

Запуск:  python tools/build_preview.py textbook-src/czas-przyszly  [выходной.html]
По умолчанию пишет <папка темы>/preview.html.
"""
import json
import os
import sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
folder = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(folder, "preview.html")

topic = json.load(open(os.path.join(folder, "topic.json"), encoding="utf-8"))
extract = json.load(open(os.path.join(folder, topic["facts_file"]), encoding="utf-8"))

data = {
    "topic": topic,
    "facts": {f["id"]: {"refs": f["refs"], "status": f.get("status", "ok")} for f in extract["facts"]},
    "sources": extract["sources"],
    "checked": date.today().strftime("%d.%m.%Y"),
}
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
tpl = open(os.path.join(here, "preview_template.html"), encoding="utf-8").read()
open(out, "w", encoding="utf-8").write(tpl.replace("__TITLE__", topic["title_pl"] + " · теория").replace("__DATA__", payload))
print("written", out)
