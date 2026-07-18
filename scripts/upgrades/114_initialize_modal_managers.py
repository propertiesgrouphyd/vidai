from pathlib import Path

file = Path("engine/app.js")

text = file.read_text(encoding="utf-8")

if "initializeApiModal();" in text and "initializePaymentModal();" in text:
    print("Already initialized")
    exit()

marker = """    initializeDropdowns();

    restoreSelections();
"""

replacement = """    initializeDropdowns();

    restoreSelections();

    initializeApiModal();

    initializePaymentModal();
"""

if marker not in text:
    print("ERROR: marker not found")
    exit(1)

text = text.replace(
    marker,
    replacement,
    1
)

file.write_text(text, encoding="utf-8")

print("Added modal initialization")
