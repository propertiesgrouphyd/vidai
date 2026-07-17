"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   Subscription Manager
   ========================================================================== */

const VWSubscription = (() => {

    let status = Object.freeze({
        active: false,
        uniqueId: "",
        expires: 0,
        checkedAt: 0
    });

    function getStatus() {
        return status;
    }

    function isActive() {
        return status.active;
    }

    function reset() {

        status = Object.freeze({
            active: false,
            uniqueId: "",
            expires: 0,
            checkedAt: Date.now()
        });

        return status;

    }

    async function refresh(uniqueId) {

        if (!uniqueId) {
            return reset();
        }

        try {

            const response = await fetch(
                `${VW_CONFIG.R2.BASE_URL}/${encodeURIComponent(uniqueId)}.json`,
                {
                    cache: "no-store"
                }
            );

            if (!response.ok) {
                return reset();
            }

            const data = await response.json();

            const expires = Number(data.expires || 0);

            status = Object.freeze({

                active: Date.now() < expires,

                uniqueId,

                expires,

                checkedAt: Date.now()

            });

            return status;

        } catch {

            return reset();

        }

    }

    return Object.freeze({

        getStatus,

        isActive,

        reset,

        refresh

    });

})();
