"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   Payment Manager
   ========================================================================== */

const VWPayment = (() => {

    async function request(endpoint, payload = {}) {

        const response = await fetch(

            VW_CONFIG.WORKER.BASE_URL + endpoint,

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify(payload)

            }

        );

        if (!response.ok) {

            throw new Error("Payment request failed.");

        }

        return response.json();

    }

    async function createOrder() {

        return request(

            VW_CONFIG.WORKER.CREATE_ORDER,

            {

                amount: VW_CONFIG.SUBSCRIPTION_PRICE

            }

        );

    }

    async function verifyPayment(data) {

        return request(

            VW_CONFIG.WORKER.VERIFY_PAYMENT,

            data

        );

    }

    return Object.freeze({

        createOrder,

        verifyPayment

    });

})();
