from pathlib import Path


# -----------------------------
# API MODAL
# -----------------------------

file = Path("engine/api-manager.js")

text = file.read_text(encoding="utf-8")

if "vw-api-close-btn" not in text:

    marker = """    const saveButton =
        document.getElementById(
            "vw-save-api-btn"
        );
"""

    insert = """
    const closeButton =
        document.getElementById(
            "vw-api-close-btn"
        );


    if (closeButton) {

        closeButton.addEventListener(
            "click",
            closeApiModal
        );

    }

"""

    if marker in text:
        text = text.replace(
            marker,
            insert + marker,
            1
        )

    else:
        print("API save button marker not found")


file.write_text(text, encoding="utf-8")



# -----------------------------
# PAYMENT MODAL
# -----------------------------

file = Path("engine/payment-manager.js")

text = file.read_text(encoding="utf-8")

if "vw-payment-close-btn" not in text:

    marker = """    const cancel =
        document.getElementById(
            "vw-payment-cancel-btn"
        );
"""

    insert = """
    const closeButton =
        document.getElementById(
            "vw-payment-close-btn"
        );


    if (closeButton) {

        closeButton.addEventListener(
            "click",
            closePaymentModal
        );

    }

"""

    if marker in text:
        text = text.replace(
            marker,
            insert + marker,
            1
        )

    else:
        print("Payment cancel marker not found")


file.write_text(text, encoding="utf-8")


print("Close button listeners added")
