<template>
  <nav class="navbar">
    <NuxtLink to="/" class="logo">🚀 LOGO-Home</NuxtLink>
    <NuxtLink to="/book" class="nav-tab">Book</NuxtLink>
    <NuxtLink to="/blog" class="nav-tab">Blog</NuxtLink>
    <NuxtLink to="/about" class="nav-tab">About Us</NuxtLink>

    <div class="nav-actions">
      <button v-if="isAuthenticated" @click="logout">Logout</button>
      <NuxtLink v-else to="/login" class="auth-button">Signup / Login</NuxtLink>
    </div>


  </nav>
</template>

<script setup>
import { ref } from "vue";
import { useState } from "#imports";
import { navigateTo } from "#app";

const isAuthenticated = useState("isAuthenticated", () => false);

const logout = () => {
  isAuthenticated.value = false; // Simulate logout
  console.log("User logged out!");
};

</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background: #333;
  color: white;
}
.logo {
  font-size: 20px;
  font-weight: bold;
  text-decoration: none;
  color: white;
}
button {
  padding: 8px 15px;
  border: none;
  cursor: pointer;
  background: #ff9800;
  color: white;
}
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  text-align: center;
}
.close {
  position: absolute;
  top: 10px;
  right: 15px;
  font-size: 20px;
  cursor: pointer;
  background: none;
  border: none;
}
.tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 15px;
}
.tabs button {
  flex: 1;
  padding: 8px;
  background: #ddd;
  border: none;
  cursor: pointer;
}
.tabs button.active {
  background: #ff9800;
  color: white;
}
</style>
