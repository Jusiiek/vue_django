interface ServiceReturnInterface {
    res: Response;
    data: any;
}

interface RequestResponse extends ServiceReturnInterface {
    headers: Headers
}

interface RequestParams {
    url: string;
    query?: Record<string, string | number | boolean>;
    headers?: Record<string, string>;
    method?: "GET" | "POST" | "PUT" | "DELETE" | "PATCH";
    body?: Record<string, any>;
    formData?: FormData;
    skipRedirect?: boolean;
    [key: string]: any;
}

interface TokenInterface {
    token: string;
}

interface UserInterface {
    id: string
    email: string
    is_staff: boolean
    is_active: boolean
    is_verified: boolean
    is_superuser: boolean
    is_global_user: boolean
    created: string
}

export type {
    RequestResponse,
    ServiceReturnInterface,
    RequestParams,
    TokenInterface,
    UserInterface
}