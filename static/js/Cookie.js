export class Cookies {

    static  getCookie(cookieName) {
        var associativearray = Cookies.allCookieList();
        return associativearray[cookieName];
    }

    static setCookie(cookieName, cookieValue, expireDate) {
        var expires = "expires=" + expireDate;
        document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
    }

    static  deleteCookie(cookieName) {
        var pastDate = new Date(0);
        pastDate = String(pastDate)
        document.cookie = cookieName + "=; expires=" + pastDate + ";path=/";
    }

    static  allCookieList() {
        var associativearray = {};
        var cookie = document.cookie.split(";");
        for (var i = 0; i < cookie.length; i++) {
            associativearray[cookie[i].split("=")[0].trim()] = cookie[i].split("=")[1].trim();
        }
        return associativearray;
    }

    static  hasCookie(cookieName) {
        return getCookie(cookieName) != null;
    }

    static deleteAllCookies() {
        var allCookies = document.cookie.split(';');
        for (var i = 0; i < allCookies.length; i++)
            document.cookie = allCookies[i] + "=;expires="
                + new Date(0).toUTCString();
    }

}