export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.hook('app:error', async (error) => {
      if (error.statusCode === 401) {
        console.log("Access token expired, refreshing...");
        
        try {
          await $fetch('/api/auth/refresh/', {
            method: 'POST',
            credentials: 'include', // Important for cookies
          });
  
          console.log("Token refreshed! Retrying request...");
          return navigateTo(nuxtApp.$route.fullPath); // Reload page with new token
        } catch (refreshError) {
          console.error("Refresh token failed:", refreshError);
          return navigateTo('/login'); // Redirect if refresh fails
        }
      }
    });
  });