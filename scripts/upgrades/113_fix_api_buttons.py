from pathlib import Path

file = Path("engine/api-manager.js")

text = file.read_text(encoding="utf-8")


# Add link button reference after saveButton
if 'id="vw-api-link-btn"' not in text:

    marker = '''    const saveButton =
        document.getElementById(
            "vw-save-api-btn"
        );

'''

    insert = '''    const saveButton =
        document.getElementById(
            "vw-save-api-btn"
        );


    const linkButton =
        document.getElementById(
            "vw-api-link-btn"
        );

'''

    text = text.replace(
        marker,
        insert,
        1
    )


# Add Groq button action
if "console.groq.com/keys" not in text:

    marker = '''    if (saveButton) {

'''

    insert = '''    if (linkButton) {

        linkButton.addEventListener(
            "click",
            () => {

                window.open(
                    "https://console.groq.com/keys",
                    "_blank",
                    "noopener,noreferrer"
                );

            }
        );

    }


'''

    text = text.replace(
        marker,
        insert + marker,
        1
    )


# Replace save action
old = '''                saveApiKey(
                    input.value
                );

                closeApiModal();
'''

new = '''                const key =
                    input.value.trim();


                if (!key) {

                    input.focus();

                    return;

                }


                saveApiKey(
                    key
                );


                closeApiModal();


                const generateButton =
                    document.getElementById(
                        "vw-generate-btn"
                    );


                if (generateButton) {

                    setTimeout(
                        () => generateButton.click(),
                        100
                    );

                }
'''

if old in text:

    text = text.replace(
        old,
        new,
        1
    )


file.write_text(text, encoding="utf-8")

print("API buttons updated")
