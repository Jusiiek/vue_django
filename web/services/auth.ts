import { useBaseUrl } from "~/constant/config";
import { request, RequestResponse } from "~/utils/request";


class Auth {
    async login(email: string, is_global=false): Promise<RequestResponse> {
        return await request({
            url: `${useBaseUrl(is_global)}auth/login/`,
            body: {email},
            method: "POST"
        })
    }
}

export const AuthService = new Auth();
