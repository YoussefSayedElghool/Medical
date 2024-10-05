import { Cookies } from "./Cookie.js";
import { TokenConst } from "./TokenConst.js";

export class TokenHandel {

    static setToken(jwtToken, refreshToken, refreshTokenExpiration) {
        const now = new Date()
        const exp = now.setMinutes(now.getMinutes() + 10);

        Cookies.setCookie(TokenConst.token, jwtToken, exp)
        Cookies.setCookie(TokenConst.refreshToken, refreshToken, refreshTokenExpiration);
    }

    static getToken() {
        return Cookies.getCookie(TokenConst.token)
    }

    static revokeToken() {
        Cookies.deleteCookie(TokenConst.token)
        Cookies.deleteCookie(TokenConst.refreshToken)
    }

     getRefreshToken() {
        return Cookies.getCookie(TokenConst.refreshToken)
    }
}