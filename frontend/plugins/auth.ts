// export default defineNuxtPlugin((nuxtApp) => {
//     const authConfig = {
//       strategies: {
//         local: {
//           token: {
//             property: "access",
//             required: true,
//             type: "Bearer",
//           },
//           refreshToken: {
//             property: "refresh",
//             data: "refresh",
//           },
//           user: {
//             property: false,  // No user endpoint needed
//             autoFetch: false,
//           },
//           endpoints: {
//             login: { url: "/api/login/", method: "post" },
//             logout: { url: "/api/logout/", method: "post" },
//             user: false, // No user endpoint needed
//           },
//         },
//       },
//     };
  
//     // Provide the auth config globally
//     nuxtApp.provide("authConfig", authConfig);
//   });
  
export default defineNuxtPlugin((nuxtApp) => {
    const auth = {
      login: () => {
        localStorage.setItem("auth", "true");
      },
      logout: () => {
        localStorage.removeItem("auth");
      },
      isAuthenticated: () => !!localStorage.getItem("auth"),
    };
  
    nuxtApp.provide("auth", auth);
  });
  