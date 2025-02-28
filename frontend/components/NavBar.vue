<template>
    <nav>
      <div class="auth">
        <span v-if="auth.loggedIn">Welcome!</span>
        <button v-if="auth.loggedIn" @click="logout">Logout</button>
        <NuxtLink v-else to="/login">Login</NuxtLink>
        <NuxtLink v-else to="/signup">Signup</NuxtLink>
      </div>
      <div class="logo">Service</div>
      <div class="menu">
        <NuxtLink to="/">Home</NuxtLink>
        <NuxtLink to="/book">Book Now</NuxtLink>
      </div>
    </nav>
  </template>
  
  <script setup>
    const auth = useAuth();
    const logout = async () => {
      await auth.logout();
      navigateTo("/login");
    };
  </script>
  
  <style scoped>
  nav {
    position: absolute;
    top: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    background: rgba(0, 0, 0, 0.5); /* ✅ Transparent background */
    color: white;
    font-weight: bold;
  }
  
  .auth button {
  background: red;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  }

  .logo {
    font-size: 24px;
    font-family: "Arial", sans-serif;
  }
  
  .menu a {
    color: white;
    text-decoration: none;
    margin-left: 20px;
    font-size: 18px;
  }
  
  .menu a:hover {
    text-decoration: underline;
  }
  </style>
  