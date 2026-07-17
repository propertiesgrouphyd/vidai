from pathlib import Path

file = Path("config.js")

text = file.read_text(encoding="utf-8")

text = text.replace(
    'const VW_CONFIG = Object.freeze({',
    'window.VW_CONFIG = Object.freeze({'
)

file.write_text(text, encoding="utf-8")

print("VW_CONFIG exposed globally")
