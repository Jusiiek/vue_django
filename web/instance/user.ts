import type {TokenInterface, UserInterface} from "~/interfaces";

class User {
    private user: UserInterface | null = null;
    private tokenData: TokenInterface | null = null;
    private userKey = "vue_django_user";
    private tokenKey = "vue_django_token";

    get() {
        if (process.client) {
            if (this.user) {
                return this.user;
            }

            const savedUser = localStorage.getItem(this.userKey);
            if (savedUser) {
                this.user = JSON.parse(savedUser);
                if (this.user) this.set(this.user);
            }

            const savedToken = localStorage.getItem(this.tokenKey);
            if (savedToken) {
                this.tokenData = JSON.parse(savedToken);
                if (this.tokenData) this.setToken(this.tokenData);
            }
        }
    }

    set(userData: UserInterface) {
        if (process.client) {
            localStorage.setItem(this.userKey, JSON.stringify(userData));
            this.user = userData;
        }
    }

    setToken(tokenData: TokenInterface) {
        if (process.client) {
            localStorage.setItem(this.tokenKey, JSON.stringify(tokenData));
            this.tokenData = tokenData
        }
    }

    clear() {
        if (process.client) {
            localStorage.removeItem(this.userKey);
            localStorage.removeItem(this.tokenKey);
        }
        this.user = null;
        this.tokenData = null;
    }

    getUser() {
        this.get()
        return this.user;
    }

    getToken() {
        this.get()
        return this.tokenData?.token;
    }

    isGlobalUser() {
        this.get();
        return this.user?.is_global_user;
    }
}

export const ActiveUser = new User();
