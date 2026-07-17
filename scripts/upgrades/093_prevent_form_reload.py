from pathlib import Path

file = Path("engine/app.js")

text = file.read_text(encoding="utf-8")

old = '''
    if (button) {
        button.addEventListener("click", onGenerate);
    }
'''

new = '''
    if (button) {

        button.addEventListener(
            "click",
            (event) => {

                event.preventDefault();

                onGenerate();

            }
        );

    }
'''

text = text.replace(old, new)

file.write_text(text, encoding="utf-8")

print("Generate reload prevented")
