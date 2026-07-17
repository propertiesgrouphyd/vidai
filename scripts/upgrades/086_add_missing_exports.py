from pathlib import Path

files = {
    "purposes.js": "VW_PURPOSES",
    "categories.js": "VW_CATEGORIES",
    "topics.js": "VW_TOPICS",
    "goals.js": "VW_GOALS",
    "content-styles.js": "VW_CONTENT_STYLES",
    "audiences.js": "VW_AUDIENCES",
    "lengths.js": "VW_LENGTHS",
    "platforms.js": "VW_PLATFORMS",
    "languages.js": "VW_LANGUAGES",
    "creativity.js": "VW_CREATIVITY",
    "emojis.js": "VW_EMOJIS",
    "ctas.js": "VW_CTAS",
}

root = Path("data")

for filename, variable in files.items():
    path = root / filename
    text = path.read_text(encoding="utf-8")

    if "export default" not in text:
        text = text.rstrip() + f"\n\nexport default {variable};\n"
        path.write_text(text, encoding="utf-8")
        print(f"Updated {filename}")
    else:
        print(f"Already OK: {filename}")
