from pathlib import Path

def replace_api(text):
    old = '''
function openApiModal() {

    const modal =
        document.getElementById(
            "vw-api-modal"
        );

    if (modal) {

        modal.hidden = false;

    }

}
'''
    new = '''
function openApiModal() {

    const modal =
        document.getElementById(
            "vw-api-modal"
        );

    if (!modal) return;

    modal.hidden = false;
    modal.setAttribute(
        "aria-hidden",
        "false"
    );

    document.body.style.overflow = "hidden";

}
'''
    return text.replace(old, new)

def replace_api_close(text):
    old = '''
function closeApiModal() {

    const modal =
        document.getElementById(
            "vw-api-modal"
        );

    if (modal) {

        modal.hidden = true;

    }

}
'''
    new = '''
function closeApiModal() {

    const modal =
        document.getElementById(
            "vw-api-modal"
        );

    if (!modal) return;

    modal.hidden = true;
    modal.setAttribute(
        "aria-hidden",
        "true"
    );

    document.body.style.overflow = "";

}
'''
    return text.replace(old, new)

def replace_payment(text):
    old = '''
    if (modal) {

        modal.hidden = false;
        modal.setAttribute(
            "aria-hidden",
            "false"
        );

    }
'''
    new = '''
    if (!modal) return;

    modal.hidden = false;

    modal.setAttribute(
        "aria-hidden",
        "false"
    );

    document.body.style.overflow = "hidden";
'''
    return text.replace(old, new)

def replace_payment_close(text):
    old = '''
    if (modal) {

        modal.hidden = true;
        modal.setAttribute(
            "aria-hidden",
            "true"
        );

    }
'''
    new = '''
    if (!modal) return;

    modal.hidden = true;

    modal.setAttribute(
        "aria-hidden",
        "true"
    );

    document.body.style.overflow = "";
'''
    return text.replace(old, new)

api = Path("engine/api-manager.js")
txt = api.read_text(encoding="utf-8")
txt = replace_api(txt)
txt = replace_api_close(txt)

if 'modal.addEventListener(' not in txt:
    txt = txt.replace(
        "    }\n\n}\n\n\nexport",
        '''
    }

    const modal =
        document.getElementById(
            "vw-api-modal"
        );

    if (modal) {

        modal.addEventListener(
            "click",
            e => {

                if (
                    e.target === modal
                ) {

                    closeApiModal();

                }

            }
        );

    }

}


export'''
    )

api.write_text(txt, encoding="utf-8")

pay = Path("engine/payment-manager.js")
txt = pay.read_text(encoding="utf-8")
txt = replace_payment(txt)
txt = replace_payment_close(txt)

if 'modal.addEventListener(' not in txt:
    txt = txt.replace(
        "    }\n\n}\n\n\nexport",
        '''
    }

    const modal =
        document.getElementById(
            "vw-payment-modal"
        );

    if (modal) {

        modal.addEventListener(
            "click",
            e => {

                if (
                    e.target === modal
                ) {

                    closePaymentModal();

                }

            }
        );

    }

}


export'''
    )

pay.write_text(txt, encoding="utf-8")

print("Modal behaviour upgraded.")
