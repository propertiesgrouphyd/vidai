from pathlib import Path

file = Path("engine/app.js")

text = file.read_text(encoding="utf-8")

text = text.replace(
    'vw-regenerate-bt");',
    'vw-regenerate-btn");'
)

file.write_text(text, encoding="utf-8")

print("Fixed exact regenerate button ID")
