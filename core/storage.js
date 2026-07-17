"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   Local Storage Manager
   ========================================================================== */

const VWStorage = (() => {

    function has(key) {
        return localStorage.getItem(key) !== null;
    }

    function remove(key) {
        localStorage.removeItem(key);
    }

    function clear() {
        localStorage.clear();
    }

    function keys() {
        return Object.keys(localStorage);
    }

    function size() {
        return localStorage.length;
    }

    function setString(key, value) {
        localStorage.setItem(key, String(value));
        return true;
    }

    function getString(key, fallback = "") {
        const value = localStorage.getItem(key);
        return value === null ? fallback : value;
    }

    function setNumber(key, value) {
        localStorage.setItem(key, String(Number(value)));
        return true;
    }

    function getNumber(key, fallback = 0) {
        const value = Number(localStorage.getItem(key));
        return Number.isFinite(value) ? value : fallback;
    }

    function setObject(key, value) {
        localStorage.setItem(key, JSON.stringify(value));
        return true;
    }

    function getObject(key, fallback = null) {
        try {
            const value = localStorage.getItem(key);
            return value === null ? fallback : JSON.parse(value);
        } catch {
            return fallback;
        }
    }

    function set(key, value) {
        return setObject(key, value);
    }

    function get(key, fallback = null) {
        return getObject(key, fallback);
    }

    function toggle(key) {
        const value = !getObject(key, false);
        setObject(key, value);
        return value;
    }

    return Object.freeze({

        has,
        remove,
        clear,

        keys,
        size,

        get,
        set,

        getString,
        setString,

        getNumber,
        setNumber,

        getObject,
        setObject,

        toggle

    });

})();
