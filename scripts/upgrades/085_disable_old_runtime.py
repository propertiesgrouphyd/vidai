from pathlib import Path

file = Path("index.html")

text = file.read_text(encoding="utf-8")

old_scripts = [
    '    <script defer src="data/library.js"></script>',
    '    <script defer src="core/storage.js"></script>',
    '    <script defer src="core/dropdown.js"></script>',
    '    <script defer src="core/subscription.js"></script>',
    '    <script defer src="core/payment.js"></script>',
    '    <script defer src="core/prompt.js"></script>',
    '    <script defer src="core/ai.js"></script>',
    '    <script defer src="core/ui.js"></script>',
    '    <script defer src="app.js"></script>',
]

for script in old_scripts:
    text = text.replace(
        script,
        "<!-- DISABLED OLD SYSTEM -->"
    )

file.write_text(text, encoding="utf-8")

print("Old runtime scripts disabled")
