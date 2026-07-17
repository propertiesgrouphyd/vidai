from pathlib import Path

file = Path("engine/app.js")

lines = file.read_text(encoding="utf-8").splitlines()

new_lines = []

for line in lines:
    if "const regenerateButton" in line:
        line = '    const regenerateButton = document.getElementById("vw-regenerate-btn");'
    new_lines.append(line)

file.write_text(
    "\n".join(new_lines) + "\n",
    encoding="utf-8"
)

print("Regenerate button line fixed")
