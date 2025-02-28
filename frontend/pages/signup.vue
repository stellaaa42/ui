<template>
  <div class="auth-container">
    <h2>Signup</h2>
    <form @submit.prevent="signup">
      <input v-model="username" type="text" placeholder="Username" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Signup</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
const { $axios } = useNuxtApp();

const username = ref("");
const email = ref("");
const password = ref("");
const errorMessage = ref("");
const auth = useAuth();

const signup = async () => {
  try {
    const response = await $axios.post("/signup/", {
      username: username.value,
      email: email.value,
      password: password.value
    });

    if (response.data.access) {
      await auth.setUserToken(response.access, response.refresh);
      navigateTo("/longin");
    }
  } catch (err) {
    errorMessage.value = err.response._data.error || "Signup failed";
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
  background: green;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
