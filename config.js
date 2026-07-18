"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   Global Configuration
   ========================================================================== */

window.VW_CONFIG = Object.freeze({

    APP_NAME: "VIDHWAAN AI Writer",
    APP_VERSION: "1.0.0",
    APP_AUTHOR: "VIDHWAAN",
    APP_URL: "https://app.vidhwaan.com",

    STORAGE_KEYS: Object.freeze({

        API_KEY: "vw_api_key",
        SETTINGS: "vw_settings",
        HISTORY: "vw_history",
        THEME: "vw_theme"

    }),

    API: Object.freeze({

        BASE_URL: "https://api.groq.com/openai/v1",
        CHAT_ENDPOINT: "/chat/completions",
        MODEL: "llama-3.3-70b-versatile"

    }),

    LIMITS: Object.freeze({

        MAX_PROMPT: 50000,
        MAX_HISTORY: 100

    }),

    UI: Object.freeze({

        LOADING_DELAY: 300,
        TOAST_TIME: 3000

    })

});