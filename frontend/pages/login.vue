<template>
  <div class="auth-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref, useNuxtApp } from "vue";
const { $axios, $authConfig } = useNuxtApp();;

const username = ref("");
const password = ref("");
const errorMessage = ref("");
const auth = useAuth();

const login = async () => {
    try {
        const response = await $axios.post("/api/login/", {
        username: username.value,
        password: password.value,
    });

    if (response.data.access) {
      navigateTo("/");
    }
  } catch (err) {
    errorMessage.value = "Invalid credentials";
  }
};
</script>

<style scoped>
.auth-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
}
input {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 5px 0;
}
button {
  width: 100%;
  padding: 10px;
  background: blue;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
