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

}


export {

    getApiKey,
    saveApiKey,
    ensureApiKey,
    initializeApiModal

};
