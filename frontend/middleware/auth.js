// export default defineNuxtRouteMiddleware((to, from) => {
//   const accessToken = useCookie("access_token"); 

//   console.log("🚀 Navigating to:", to.path);
//   console.log("🔑 Access Token:", accessToken.value ? "✅ Exists" : "❌ Missing");

//   if (!accessToken.value && to.path !== "/") {
//     console.warn("⛔ No token! Redirecting to /");
//     return navigateTo("/");
//   }

//   console.log("✅ Allowed: Proceeding to", to.path);
// });
