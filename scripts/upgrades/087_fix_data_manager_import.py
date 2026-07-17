from pathlib import Path

file = Path("engine/data-manager.js")

text = file.read_text(encoding="utf-8")

old = 'import data from "../data/index.js";'
new = 'import * as data from "../data/index.js";'

if old in text:
    text = text.replace(old, new)
    file.write_text(text, encoding="utf-8")
    print("Updated data-manager.js")
else:
    print("Import already updated or not found.")
