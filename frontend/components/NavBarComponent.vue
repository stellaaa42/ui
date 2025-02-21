<template>
    <nav>
      <div class="logo">Service</div>
      <div class="menu">
        <NuxtLink to="/">Home</NuxtLink>
        <NuxtLink to="/book">Book Now</NuxtLink>
      </div>
    </nav>
  </template>
  
  <script setup>
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
  