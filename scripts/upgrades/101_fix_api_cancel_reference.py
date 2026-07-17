from pathlib import Path

file = Path("engine/api-manager.js")

text = file.read_text(encoding="utf-8")

old = '''
    const cancelButton =
        document.getElementById(
            "vw-api-cancel-btn"
        );


'''

text = text.replace(old, "")


old_block = '''
    if (cancelButton) {

        cancelButton.addEventListener(
            "click",
            closeApiModal
        );

    }

'''

text = text.replace(old_block, "")

file.write_text(text, encoding="utf-8")

print("Removed invalid API cancel reference")
