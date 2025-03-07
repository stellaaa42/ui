<template>
  <div class="auth-container">
    <h2>Login</h2>

    <!-- OAuth Login Buttons -->
    <div class="oauth-buttons">
      <button @click="oauthLogin('google')">Login with Google</button>
    </div>

    <!-- Login Form -->
    <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />

      <button type="submit" :disabled="loading">
        {{ loading ? "Logging in..." : "Login" }}
      </button>
    </form>

    <!-- Status Messages -->
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useFetch, useRouter, useCookie } from "#app";

const router = useRouter();
const username = ref("");
const password = ref("");
const successMessage = ref("");
const errorMessage = ref("");
const loading = ref(false);

// Function to login user
const login = async () => {
  errorMessage.value = "";
  successMessage.value = "";
  loading.value = true;

  try {
    const { data, error } = await useFetch("/auth/login", {
      method: "POST",
      body: { username: username.value, password: password.value },
    });

    if (data.value?.access) {
      successMessage.value = "Login successful! Redirecting...";
      useCookie("user").value = data.value.user; // Store user in a cookie

      setTimeout(() => {
        router.push("/");
      }, 1500);
    } else {
      errorMessage.value = error.value?.message || "Invalid credentials";
    }
  } catch (err) {
    errorMessage.value = "Login failed. Please try again.";
  } finally {
    loading.value = false;
  }
};

// Function to handle OAuth login
const oauthLogin = async (provider) => {
  try {
    const { data, error } = await useFetch(`/auth/oauth?provider=${provider}`);

    if (data.value?.authorization_url) {
      window.location.href = data.value.authorization_url;
    } else {
      errorMessage.value = "OAuth login failed. Try again.";
    }
  } catch {
    errorMessage.value = "OAuth login error.";
  }
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
