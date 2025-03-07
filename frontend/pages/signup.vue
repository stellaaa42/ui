<script setup>
import { ref } from 'vue';
import { useFetch } from '#app';

const username = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const message = ref('');

const signup = async () => {
  if (password.value !== confirmPassword.value) {
    message.value = "Passwords don't match!";
    return;
  }

  const { data, error } = await useFetch('/auth/signup', {
    method: 'POST',
    body: {
      username: username.value,
      email: email.value,
      password1: password.value,
      password2: confirmPassword.value,
    },
  });

  if (data.value) {
    message.value = "Signup successful! You can now log in.";
  } else {
    message.value = error.value || "Signup failed.";
  }
};
</script>

<template>
  <div>
    <h1>Sign Up</h1>
    <input v-model="username" placeholder="Username" />
    <input v-model="email" placeholder="Email" type="email" />
    <input v-model="password" placeholder="Password" type="password" />
    <input v-model="confirmPassword" placeholder="Confirm Password" type="password" />
    <button @click="signup">Sign Up</button>
    
    <p v-if="message">{{ message }}</p>
  </div>
</template>
