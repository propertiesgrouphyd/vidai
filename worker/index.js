const CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type"
};

const SUBSCRIPTION_PRICE = 3000; // ₹30 (paise)
const SUBSCRIPTION_DAYS = 30;

function json(data, status = 200) {
    return new Response(
        JSON.stringify(data),
        {
            status,
            headers: {
                "Content-Type": "application/json",
                ...CORS_HEADERS
            }
        }
    );
}

async function body(request) {
    try {
        return await request.json();
    } catch {
        return {};
    }
}

function requireFields(data, fields) {
    for (const field of fields) {
        if (
            data[field] === undefined ||
            data[field] === null ||
            data[field] === ""
        ) {
            throw new Error("Missing field: " + field);
        }
    }
}

function generateReceipt() {
    return (
        "VW-" +
        Date.now().toString(36).toUpperCase() +
        "-" +
        crypto.randomUUID()
            .replace(/-/g, "")
            .substring(0, 8)
            .toUpperCase()
    );
}

export default {

    async fetch(request, env) {

        if (request.method === "OPTIONS") {
            return new Response(null, {
                headers: CORS_HEADERS
            });
        }

        try {

            const url = new URL(request.url);

            if (
                request.method === "POST" &&
                url.pathname === "/create-order"
            ) {

                const order =
                    await createRazorpayOrder(env);

                return json({
                    success: true,
                    order
                });

            }

            if (
                request.method === "POST" &&
                url.pathname === "/verify-payment"
            ) {

                const data =
                    await body(request);

                requireFields(data, [
                    "unique_id",
                    "razorpay_order_id",
                    "razorpay_payment_id",
                    "razorpay_signature"
                ]);

                const valid =
                    await verifySignature(
                        env,
                        data.razorpay_order_id,
                        data.razorpay_payment_id,
                        data.razorpay_signature
                    );

                if (!valid) {
                    return json({
                        success: false,
                        message:
                            "Invalid payment signature."
                    }, 400);
                }

                const expires =
                    await writeSubscription(
                        env,
                        data.unique_id
                    );

                await purgeSubscription(
                    env,
                    data.unique_id
                );

                return json({
                    success: true,
                    expires
                });

            }

            return json({
                success: false,
                message: "Not Found"
            }, 404);

        } catch (error) {

            return json({
                success: false,
                message: error.message
            }, 500);

        }

    }

};

