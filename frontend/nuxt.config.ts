export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiBase: "http://localhost:8000/api", // ✅ Change this for production
    },
  },
  modules: [],
  css: [],
  build: {},
  compatibilityDate: "2025-02-22",
});
