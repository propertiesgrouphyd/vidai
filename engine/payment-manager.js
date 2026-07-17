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
            () => {

                console.log(
                    "Payment flow started"
                );

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
