function openPaymentModal() {

    const modal =
        document.getElementById(
            "vw-payment-modal"
        );

    if (modal) {

        modal.hidden = false;
        modal.setAttribute(
            "aria-hidden",
            "false"
        );

    }

}


function closePaymentModal() {

    const modal =
        document.getElementById(
            "vw-payment-modal"
        );

    if (modal) {

        modal.hidden = true;
        modal.setAttribute(
            "aria-hidden",
            "true"
        );

    }

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

}


export {

    openPaymentModal,
    closePaymentModal,
    initializePaymentModal

};
