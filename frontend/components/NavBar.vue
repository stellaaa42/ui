<template>
  <nav class="navbar">
    <NuxtLink to="/" class="logo">🚀 MyApp</NuxtLink>

    <div class="nav-actions">
      <button v-if="isAuthenticated" @click="logout">Logout</button>
      <button v-else @click="showAuthModal = true">Signup / Login</button>
    </div>

    <!-- Auth Modal (Login & Signup Tabs) -->
    <div v-if="showAuthModal" class="modal">
      <div class="modal-content">
        <button class="close" @click="showAuthModal = false">×</button>

        <div class="tabs">
          <button @click="activeTab = 'login'" :class="{ active: activeTab === 'login' }">Login</button>
          <button @click="activeTab = 'signup'" :class="{ active: activeTab === 'signup' }">Signup</button>
        </div>

        <div v-if="activeTab === 'login'">
          <LoginForm @loginSuccess="handleAuthSuccess" />
        </div>
        <div v-if="activeTab === 'signup'">
          <SignupForm @signupSuccess="handleAuthSuccess" />
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";
import { useNuxtApp } from "#app";
import LoginForm from "@/components/LoginForm.vue";
import SignupForm from "@/components/SignupForm.vue";

const { $auth } = useNuxtApp();
const isAuthenticated = ref($auth.isAuthenticated);
const showAuthModal = ref(false);
const activeTab = ref("login"); // Default to Login tab

const logout = () => {
  $auth.logout();
};

const handleAuthSuccess = () => {
  showAuthModal.value = false; // Close modal after successful login/signup
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
