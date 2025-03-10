<template>
  <div class="signup-container">
    <h1>Sign Up</h1>

    <!-- Signup Form -->
    <form @submit.prevent="signup" class="signup-form">
      <div class="form-group">
        <label for="username">Username:</label>
        <input id="username" v-model.trim="username" required />
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input id="email" v-model.trim="email" type="email" required />
      </div>

      <div class="form-group">
        <label for="password">Password:</label>
        <input id="password" v-model="password" type="password" required />
      </div>

      <div class="form-group">
        <label for="confirmPassword">Confirm Password:</label>
        <input id="confirmPassword" v-model="confirmPassword" type="password" required />
      </div>

      <button type="submit" :disabled="loading">
        {{ loading ? "Signing up..." : "Sign Up" }}
      </button>
    </form>

    <!-- Error & Success Messages -->
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>

    <!-- Redirect to Login -->
    <p>Already have an account? <NuxtLink to="/login" class="link">Login</NuxtLink></p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useFetch } from "#app";

const router = useRouter();
const username = ref("");
const email = ref("");
const password = ref("");
const confirmPassword = ref("");
const loading = ref(false);
const errorMessage = ref("");
const successMessage = ref("");

const signup = async () => {
  errorMessage.value = "";
  successMessage.value = "";

  if (!username.value || !email.value || !password.value) {
    errorMessage.value = "All fields are required.";
    return;
  }

  if (!email.value.includes("@")) {
    errorMessage.value = "Invalid email format.";
    return;
  }

  if (password.value.length < 6) {
    errorMessage.value = "Password must be at least 6 characters long.";
    return;
  }

  if (password.value !== confirmPassword.value) {
    errorMessage.value = "Passwords do not match.";
    return;
  }

  loading.value = true;

  try {
    const { data, error } = await useFetch("/auth/signup", {
      method: "POST",
      body: {
        username: username.value,
        email: email.value,
        password1: password.value,
        password2: confirmPassword.value,
      },
    });

    if (error.value) {
      errorMessage.value = error.value.data?.message || "Signup failed. Please try again.";
      return;
    }

    successMessage.value = "Signup successful! Redirecting to login...";
    setTimeout(() => router.push("/login"), 2000);
  } catch (err) {
    errorMessage.value = "Unexpected error occurred.";
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
/* Container */
.signup-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 2rem;
  border-radius: 10px;
  background: white;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

/* Form */
.signup-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Form Group */
.form-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

/* Labels */
.form-group label {
  font-weight: bold;
  margin-bottom: 5px;
}

/* Inputs */
.form-group input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
  outline: none;
  transition: 0.2s;
}

.form-group input:focus {
  border-color: #ffcc00;
}

/* Submit Button */
button {
  background: blue;
  border: none;
  padding: 0.7rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 5px;
  transition: 0.3s;
}

button:hover {
  background: rgb(212, 0, 255);
}

button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

/* Error & Success Messages */
.error {
  color: red;
  font-weight: bold;
}

.success {
  color: green;
  font-weight: bold;
}

/* Links */
.link {
  color: #007bff;
  text-decoration: none;
  font-weight: bold;
}

.link:hover {
  text-decoration: underline;
}
</style>
