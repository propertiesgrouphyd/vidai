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

    if (!modal) return;

    modal.hidden = false;
    modal.setAttribute(
        "aria-hidden",
        "false"
    );

    document.body.style.overflow = "hidden";

}


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


export {

    getApiKey,
    saveApiKey,
    ensureApiKey,
    initializeApiModal

};
