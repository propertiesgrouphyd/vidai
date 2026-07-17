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

    SUBSCRIPTION_PRICE: 30,
    SUBSCRIPTION_DAYS: 30,

    STORAGE_KEYS: Object.freeze({
        API_KEY: "vw_api_key",
        UNIQUE_ID: "vw_unique_id",
        SETTINGS: "vw_settings",
        HISTORY: "vw_history",
        THEME: "vw_theme",
        LAST_CHECK: "vw_last_check"
    }),

    API: Object.freeze({
        BASE_URL: "https://api.groq.com/openai/v1",
        CHAT_ENDPOINT: "/chat/completions",
        MODEL: "llama-3.3-70b-versatile"
    }),

    WORKER: Object.freeze({
        BASE_URL: "https://bold-fire-78f8.propertiesgrouphyd.workers.dev",
        CREATE_ORDER: "/create-order",
        VERIFY_PAYMENT: "/verify-payment"
    }),

    R2: Object.freeze({
        BASE_URL: "https://subscriptions.propertiesgrouphyd.online/subscriptions"
    }),

    SUBSCRIPTION: Object.freeze({
        CACHE_MINUTES: 15
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
