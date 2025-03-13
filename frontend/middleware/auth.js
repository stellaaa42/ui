export default defineNuxtRouteMiddleware((to, from) => {
  if (process.client) return

  const token = useCookie("token"); 

  if (token.value && to.path === "/login") {
    console.log("Redirecting to /dashboard");
    return navigateTo("/dashboard");
  } else {
    console.log("Navigating to:", to.path);
    navigateTo("/");
  }

  console.log("✅ Allowed: Proceeding to", to.path);
});
