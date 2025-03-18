<script setup>
const logout = async () => {
  try {
    // console.log('logout.vue user cookie:', useCookie("user").value);
    // useCookie("user").value = null;
    await $fetch("/api/auth/logout", { method: "POST" });
    console.log("You logged out!");
    navigateTo("/"); 
  } catch (error) {
    console.error("Logout failed:", error);
  }
};

// Call logout when the page loads
logout();
</script>

<template>
  <div class="flex items-center justify-center h-screen">
    <p class="text-lg">Logging out...</p>
  </div>
</template>
