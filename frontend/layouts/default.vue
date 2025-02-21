<!-- layouts/default.vue -->
<template>
    <div>
      <NavBarComponent />
      <NuxtPage /> <!-- Renders page components -->
    </div>
  </template>
  
  <script setup>
  import NavBarComponent from '~/components/NavBarComponent.vue'
  </script>
  
  <style>
  body {
    margin: 0;
    font-family: Arial, sans-serif;
  }
  </style>