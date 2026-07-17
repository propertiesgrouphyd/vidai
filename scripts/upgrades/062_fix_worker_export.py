from pathlib import Path
import re

file = Path("worker/index.js")
text = file.read_text(encoding="utf-8")

matches = list(re.finditer(r'export\s+default\s*\{', text))

if len(matches) != 2:
    raise SystemExit(f"Expected 2 export default blocks, found {len(matches)}")

start1 = matches[0].start()
start2 = matches[1].start()

# Keep everything before the first export,
# then append the second (complete) export block.
fixed = text[:start1].rstrip() + "\n\n" + text[start2:]

file.write_text(fixed, encoding="utf-8")

print("✓ Removed duplicate export block.")
