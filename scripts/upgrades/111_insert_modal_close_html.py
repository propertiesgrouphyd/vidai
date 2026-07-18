from pathlib import Path

file = Path("index.html")

text = file.read_text(encoding="utf-8")


# API modal
if "vw-api-close-btn" not in text:

    text = text.replace(
        '<div class="vw-modal-card">\n\n            <h2 id="vw-api-title">',
        '''<div class="vw-modal-card">

            <button
                class="vw-modal-close"
                id="vw-api-close-btn"
                type="button"
                aria-label="Close">

                &times;

            </button>

            <h2 id="vw-api-title">''',
        1
    )


# Payment modal
if "vw-payment-close-btn" not in text:

    text = text.replace(
        '<div class="vw-modal-card">\n\n            <h2 id="vw-payment-title">',
        '''<div class="vw-modal-card">

            <button
                class="vw-modal-close"
                id="vw-payment-close-btn"
                type="button"
                aria-label="Close">

                &times;

            </button>

            <h2 id="vw-payment-title">''',
        1
    )


file.write_text(text, encoding="utf-8")

print("HTML modal close buttons patch completed")
