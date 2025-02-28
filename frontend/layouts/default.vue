<template>
  <div>
    <header>
      <h1>Service</h1>
    </header>
    <Navbar />
    <NuxtPage />
  </div>
</template>

<style scoped>
header {
  background-color: #f5f5f5;
  padding: 10px;
  text-align: center;
}
</style>


<script setup>
import Navbar from "~/components/NavBar.vue";
</script>
