"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   UI Helpers
   ========================================================================== */

const VWUI = (() => {

    const $ = (
        selector,
        parent = document
    ) =>
        parent.querySelector(selector);


    const $$ = (
        selector,
        parent = document
    ) =>
        [...parent.querySelectorAll(selector)];


    function showLoading() {

        const loading = $("#vw-loading");

        if (!loading) return;

        loading.hidden = false;

        loading.setAttribute(
            "aria-hidden",
            "false"
        );

    }


    function hideLoading() {

        const loading = $("#vw-loading");

        if (!loading) return;

        loading.hidden = true;

        loading.setAttribute(
            "aria-hidden",
            "true"
        );

    }


    function showToast(
        message,
        duration = 3000
    ) {

        const toast = $("#vw-toast");

        if (!toast) return;


        toast.textContent = message;

        toast.hidden = false;


        clearTimeout(
            showToast.timer
        );


        showToast.timer =
            setTimeout(() => {

                toast.hidden = true;

            }, Number(duration) || 3000);

    }


    function setText(
        selector,
        value = ""
    ) {

        const element = $(selector);

        if (element) {

            element.textContent = value;

        }

    }


    function setHTML(
        selector,
        value = ""
    ) {

        const element = $(selector);

        if (element) {

            element.innerHTML = value;

        }

    }


    function show(selector) {

        const element = $(selector);

        if (element) {

            element.hidden = false;

        }

    }


    function hide(selector) {

        const element = $(selector);

        if (element) {

            element.hidden = true;

        }

    }


    function updateSubscription(status = {}) {

        const badge =
            $("#vw-subscription-status");


        if (!badge) return;


        if (status.active) {

            badge.textContent = "Active";

            badge.dataset.state =
                "active";

        } else {

            badge.textContent = "Inactive";

            badge.dataset.state =
                "inactive";

        }

    }


    function showModal(selector) {

        show(selector);

    }


    function hideModal(selector) {

        hide(selector);

    }


    return Object.freeze({

        $,

        $$,

        showLoading,

        hideLoading,

        showToast,

        setText,

        setHTML,

        show,

        hide,

        showModal,

        hideModal,

        updateSubscription

    });


})();
