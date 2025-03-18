// export default defineNuxtRouteMiddleware((to, from) => {
//   if (!process.client) return

//   const token = useCookie("token").value;
//   const user = useCookie("user").value;

//   if (!token || !user) {
//     console.log("auth.js no token/user, navigating to /");
//     return navigateTo("/");
//   } else {
//     console.log("auth.js token:", token);
//     console.log("auth.js user:", user);
//     console.log("Navigating to:", to.path);
//     navigateTo("/dashboard");
//     return;
//   }
// });
