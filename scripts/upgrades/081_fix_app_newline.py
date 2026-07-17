from pathlib import Path

file = Path("engine/app.js")

text = file.read_text(encoding="utf-8")

text = text.replace(
    '"use strict";\\n\\n',
    '"use strict";\n\n'
)

file.write_text(text, encoding="utf-8")

print("Fixed newline characters")
