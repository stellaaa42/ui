// // https://nuxt.com/docs/api/configuration/nuxt-config
// export default defineNuxtConfig({
//   devtools: { enabled: true },
//   runtimeConfig: {
//     public: {
//       // apiBase: 'http://localhost:8000/api/' // Backend API URL
//       apiBase: '/api',
//     }
//   },

//   modules: [
//     // '@nuxtjs/tailwindcss' // Example module if you're using Tailwind
//     // '@pinia/nuxt'          // Example for state management
//   ],

//   // css: [
//   //   '~/assets/css/main.css' // Global CSS file
//   // ],

//   compatibilityDate: '2025-02-21',
//   ssr: false,
// });

export default defineNuxtConfig({
  modules: [],
  css: [],

  app: {
    head: {
      title: 'Nuxt App',
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'My Nuxt 3 Application' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  },

  vite: {
    clearScreen: false,
    server: {
      watch: {
        usePolling: true
      }
    }
  },

  compatibilityDate: '2025-02-21'
});