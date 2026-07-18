import { getUniqueId } from "./identity-manager.js";

function openPaymentModal() {

    const modal =
        document.getElementById(
            "vw-payment-modal"
        );

    if (!modal) return;

    modal.hidden = false;

    modal.setAttribute(
        "aria-hidden",
        "false"
    );

    document.body.style.overflow = "hidden";

}


function closePaymentModal() {

    const modal =
        document.getElementById(
            "vw-payment-modal"
        );

    if (!modal) return;

    modal.hidden = true;

    modal.setAttribute(
        "aria-hidden",
        "true"
    );

    document.body.style.overflow = "";

}


function initializePaymentModal() {


    const closeButton =
        document.getElementById(
            "vw-payment-close-btn"
        );


    if (closeButton) {

        closeButton.addEventListener(
            "click",
            closePaymentModal
        );

    }

    const cancel =
        document.getElementById(
            "vw-payment-cancel-btn"
        );


    if (cancel) {

        cancel.addEventListener(
            "click",
            closePaymentModal
        );

    }


    const payment =
        document.getElementById(
            "vw-payment-btn"
        );


    if (payment) {

        payment.addEventListener(
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

                                document.dispatchEvent(

                                    new CustomEvent(

                                        "vw-subscription-activated",

                                        {

                                            detail:result

                                        }

                                    )

                                );

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
        );


    }

    const modal =
        document.getElementById(
            "vw-payment-modal"
        );

    if (modal) {

        modal.addEventListener(
            "click",
            e => {

                if (
                    e.target === modal
                ) {

                    closePaymentModal();

                }

            }
        );

    }

}


export {

    openPaymentModal,
    closePaymentModal,
    initializePaymentModal

};
