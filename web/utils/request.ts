import { ActiveUser } from "@/instance/user";

export interface ServiceReturnInterface {
    res: Response;
    data: any;
}

export interface RequestParams {
    url: string;
    query?: Record<string, string | number | boolean>;
    headers?: Record<string, string>;
    method?: "GET" | "POST" | "PUT" | "DELETE" | "PATCH";
    body?: Record<string, any>;
    formData?: FormData;
    skipRedirect?: boolean;
    [key: string]: any;
}

export interface RequestResponse extends ServiceReturnInterface {
    headers: Headers
}


export const redirectIfNotAuthenticated = (res: Response) => {
  if (res.status === 401) {
    ActiveUser.clear();
    return window.location.replace("/auth/login");
  }
  if (res.status === 403) return window.location.replace("/");
};

export const encodeQuery = (query: Record<string, any>) => {
  const searchParams = new URLSearchParams(query || {});
  return searchParams.toString();
};

export const request = async ({
  url,
  query,
  headers = {},
  method = "GET",
  body,
  formData,
  skipRedirect = false,
  ...rest
}: RequestParams): Promise<RequestResponse> => {
  const methodLower = method.toLowerCase();
  const jsonMethods = ["post", "put", "patch", "delete"];
  if (body && jsonMethods.includes(methodLower) && !headers["Content-Type"]) {
    headers["Content-Type"] = "application/json";
  }

  let requestBody: BodyInit | null | undefined = undefined;
  if (formData) {
    requestBody = formData;
  } else if (body) {
    if (typeof body === "object") {
      requestBody = JSON.stringify(body);
    } else {
      requestBody = body as BodyInit;
    }
  }
  const token = ActiveUser.getToken()
  const tokenType = ActiveUser.getTokenType()
  if (token && tokenType) {
    headers.Authorization = `${tokenType} ${token}`;
  }

  if (query) {
    url = `${url}?${encodeQuery(query)}`;
  }
  const res = await fetch(url, {
    method: method,
    headers: headers,
    body: requestBody,
    credentials: "include",
    ...rest,
  });

  if (!skipRedirect) {
    redirectIfNotAuthenticated(res);
  }

  const contentType = res.headers.get("content-type");
  if (contentType !== "application/json" || res.status === 204) {
    return {
      res,
      data: {},
      headers: res.headers,
    };
  }

  const data = await res.json();

  return {
    res,
    data,
    headers: res.headers,
  };
};
