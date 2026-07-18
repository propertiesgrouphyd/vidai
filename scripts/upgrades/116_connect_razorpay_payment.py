from pathlib import Path

file = Path("engine/payment-manager.js")

text = file.read_text(encoding="utf-8")


# Add identity import
if 'identity-manager.js' not in text:

    text = (
        'import { getUniqueId } from "./identity-manager.js";\n\n'
        + text
    )


old = '''        payment.addEventListener(
            "click",
            () => {

                console.log(
                    "Payment flow started"
                );

            }
        );'''


new = '''        payment.addEventListener(
            "click",
            async () => {

                try {


                    const uniqueId =
                        getUniqueId();



                    const orderResponse =
                        await fetch(

                            window.VW_CONFIG.WORKER.BASE_URL +
                            window.VW_CONFIG.WORKER.CREATE_ORDER,

                            {

                                method:"POST",

                                headers:{
                                    "Content-Type":
                                    "application/json"
                                },

                                body:JSON.stringify({

                                    uniqueId

                                })

                            }

                        );



                    const order =
                        await orderResponse.json();



                    if (!order.orderId) {

                        throw new Error(
                            "Unable to create payment order"
                        );

                    }



                    const options = {


                        key:
                        order.key,


                        amount:
                        order.amount,


                        currency:
                        "INR",


                        name:
                        "VIDHWAAN AI",


                        description:
                        "30 Days Subscription",


                        order_id:
                        order.orderId,



                        handler:
                        async function(response){



                            const verifyResponse =
                                await fetch(

                                    window.VW_CONFIG.WORKER.BASE_URL +
                                    window.VW_CONFIG.WORKER.VERIFY_PAYMENT,

                                    {

                                        method:"POST",

                                        headers:{
                                            "Content-Type":
                                            "application/json"
                                        },

                                        body:JSON.stringify({

                                            paymentId:
                                            response.razorpay_payment_id,


                                            orderId:
                                            response.razorpay_order_id,


                                            signature:
                                            response.razorpay_signature,


                                            uniqueId

                                        })

                                    }

                                );



                            const result =
                                await verifyResponse.json();



                            if(result.success){

                                closePaymentModal();


                                window.location.reload();

                            }


                        }



                    };



                    const razorpay =
                        new Razorpay(options);



                    razorpay.open();



                }
                catch(error){

                    console.error(
                        "Payment failed:",
                        error
                    );

                    alert(
                        "Payment could not start."
                    );

                }


            }
        );'''


if old not in text:

    print("ERROR: payment click block not found")
    exit(1)


text = text.replace(
    old,
    new,
    1
)


file.write_text(text, encoding="utf-8")

print("Razorpay payment flow connected")
