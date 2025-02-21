<template>
    <div>
      <h2>{{ title }}</h2>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    title: String
  });
  </script>
  
  <style scoped>
  h2 {
    color: #35495e;
  }
  </style>