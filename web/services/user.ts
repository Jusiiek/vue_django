import { useBaseUrl } from "~/constant/config";
import { request } from "~/utils/request";
import type { RequestResponse } from '~/interfaces'


class User {
    async getUserList(): Promise<RequestResponse> {
        return await request({
            url: `${useBaseUrl()}api/users/`,
        })
    }

    async getUser(userId: string, is_global: boolean=false): Promise<RequestResponse> {
        return await request({
            url: `${useBaseUrl(is_global)}api/users/${userId}`,
        })
    }
}

export const UserService = new User();
