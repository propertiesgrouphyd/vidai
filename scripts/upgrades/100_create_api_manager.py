from pathlib import Path

file = Path("engine/api-manager.js")

content = r'''
function getApiKey() {

    return localStorage.getItem(
        window.VW_CONFIG.STORAGE_KEYS.API_KEY
    ) || "";

}


function saveApiKey(key) {

    localStorage.setItem(
        window.VW_CONFIG.STORAGE_KEYS.API_KEY,
        key.trim()
    );

}


function openApiModal() {

    const modal =
        document.getElementById(
            "vw-api-modal"
        );

    if (modal) {

        modal.hidden = false;

    }

}


function closeApiModal() {

    const modal =
        document.getElementById(
            "vw-api-modal"
        );

    if (modal) {

        modal.hidden = true;

    }

}


function ensureApiKey() {

    const key = getApiKey();


    if (!key) {

        openApiModal();

        return false;

    }


    return true;

}


function initializeApiModal() {

    const saveButton =
        document.getElementById(
            "vw-save-api-btn"
        );


    const input =
        document.getElementById(
            "vw-api-key"
        );


    const cancelButton =
        document.getElementById(
            "vw-api-cancel-btn"
        );


    if (saveButton) {

        saveButton.addEventListener(
            "click",
            () => {

                saveApiKey(
                    input.value
                );

                closeApiModal();

            }
        );

    }


    if (cancelButton) {

        cancelButton.addEventListener(
            "click",
            closeApiModal
        );

    }

}


export {

    getApiKey,
    saveApiKey,
    ensureApiKey,
    initializeApiModal

};
'''

file.write_text(
    content.strip() + "\n",
    encoding="utf-8"
)

print("Created API manager")
