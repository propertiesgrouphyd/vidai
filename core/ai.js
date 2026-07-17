"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   AI Client
   ========================================================================== */

const VWAI = (() => {

    async function generate(prompt) {

        const apiKey = VWStorage.getString(
            VW_CONFIG.STORAGE_KEYS.API_KEY,
            ""
        );

        if (!apiKey) {

            throw new Error(
                "API key not found."
            );

        }

        const response = await fetch(

            VW_CONFIG.API.BASE_URL +
            VW_CONFIG.API.CHAT_ENDPOINT,

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json",

                    "Authorization":
                        `Bearer ${apiKey}`

                },

                body: JSON.stringify({

                    model:
                        VW_CONFIG.API.MODEL,

                    messages: [

                        {

                            role: "user",

                            content: prompt

                        }

                    ],

                    temperature: 0.7,

                    max_tokens: 4096

                })

            }

        );

        if (!response.ok) {

            let message =
                "AI request failed.";

            try {

                const error =
                    await response.json();

                message =
                    error?.error?.message ||
                    message;

            } catch {}

            throw new Error(message);

        }

        const data =
            await response.json();

        return (

            data?.choices?.[0]
                ?.message
                ?.content
                ?.trim()

            || ""

        );

    }

    return Object.freeze({

        generate

    });

})();
