<template>
  <div class="auth-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useNuxtApp } from "#imports";

const { $axios } = useNuxtApp();;
const username = ref("");
const password = ref("");
const successMessage = ref("");
const errorMessage = ref("");

const login = async () => {
    try {
        const response = await $axios.post("login/", {
        username: username.value,
        password: password.value,
    });

    if (response.data.access) {
      successMessage.value = "Login successful! Redirecting...";
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
