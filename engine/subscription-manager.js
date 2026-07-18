import { getUniqueId } from "./identity-manager.js";

async function checkSubscription(uniqueId) {

    uniqueId =
        uniqueId ||
        getUniqueId();

    if (!uniqueId) {

        return {

            active: false,
            reason: "missing-id"

        };

    }


    try {

        const url =
            `${window.VW_CONFIG.R2.BASE_URL}/${encodeURIComponent(uniqueId)}.json`;


        const response =
            await fetch(
                url,
                {
                    cache: "no-store"
                }
            );


        if (!response.ok) {

            return {

                active: false,
                reason: "not-found"

            };

        }


        const data =
            await response.json();


        const expires =
            Number(data.expires || 0);


        if (
            !expires ||
            Date.now() >= expires
        ) {

            return {

                active: false,
                reason: "expired",
                expires

            };

        }


        return {

            active: true,
            expires

        };


    } catch (error) {

        console.error(
            "Subscription check failed:",
            error
        );


        return {

            active: false,
            reason: "error"

        };

    }

}


export {

    checkSubscription

};
