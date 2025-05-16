// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  modules: ['@nuxt/ui'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  css: ['./assets/css/main.css'],
  runtimeConfig: {
    public: {
      GLOBAL_API: process.env.GLOBAL_API,
      STORE_API: process.env.STORE_API,
      STORE_NAME: process.env.STORE_NAME,
    },
  }
})
