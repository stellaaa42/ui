<template>
  <div class="auth-container">
    <h2>Login</h2>

    <!-- OAuth Login Buttons -->
    <div class="oauth-buttons">
      <button @click="oauthLogin('google')">Signup/Login with Google</button>
    </div>

    <!-- Login Form -->
    <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />

      <button type="submit" :disabled="loading">
        {{ loading ? "Logging in..." : "Login" }}
      </button>
    </form>

    <NuxtLink to="/signup" no-prefetch class="btn secondary">No account? Signup</NuxtLink>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>

  </div>
</template>

<script setup>
import { ref } from "vue";
import { useFetch } from "#app";

const username = ref("");
const password = ref("");
const successMessage = ref("");
const errorMessage = ref("");
const loading = ref(false);

const login = async () => {
  errorMessage.value = "";
  successMessage.value = "";
  loading.value = true;

  try {
    const data = await $fetch("/api/auth/login", {
      method: "POST",
      body: { username: username.value, password: password.value },
      credentials: "include", 
    });
    console.log("login.vue data:", data);

    if (data) {
      successMessage.value = "Login successful!";

      console.log("login.vue useCookie user data:", data.user);
      console.log("login.vue useCookie token:", data.token);
      useCookie("user").value = data.user; 
      useCookie("token").value = data.token;

      setTimeout(() => {
        navigateTo("/dashboard");
      }, 1000);
    } else {
      errorMessage.value = "Your password or username is incorrect."; 
    }
  } catch (err) {
    console.error("Login error:", err);
    errorMessage.value = err?.message || "Login failed. Please try again.";
  } finally {
    loading.value = false;
  }
};



const oauthLogin = async () => {
    const { data, error } = await useFetch(`api/auth/oauth?provider=google`);

    if (error.value) {
    alert("OAuth Error: " + error.value.message);
    return;
  }

  window.location.href = data.value.url;
};
</script>

<style scoped>
.auth-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  text-align: center;
}

.oauth-buttons {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 15px;
}

input {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  width: 100%;
  padding: 10px;
  background: blue;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

button:disabled {
  background: gray;
  cursor: not-allowed;
}

.success {
  color: green;
  margin-top: 10px;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>
