from pathlib import Path

file = Path("index.html")

text = file.read_text(encoding="utf-8")

first = '<link rel="stylesheet" href="main.css">'

count = text.count(first)

if count > 1:
    parts = text.split(first)
    text = first + "".join(parts[1:])
    print("Removed duplicate main.css")
else:
    print("No duplicate exact link found")

file.write_text(text, encoding="utf-8")
