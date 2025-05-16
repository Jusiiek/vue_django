import { useBaseUrl } from "~/constant/config";
import { request } from "~/utils/request";
import type { RequestResponse } from '~/interfaces'


class Auth {
    async login(email: string, is_global=false): Promise<RequestResponse> {
        return await request({
            url: `${useBaseUrl(is_global)}auth/login/`,
            body: {email: email},
            method: "POST"
        })
    }
}

export const AuthService = new Auth();
