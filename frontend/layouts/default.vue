<template>
  <div>
    <header>
      <Navbar />
    </header>
  </div>
  <div>
      <slot/>
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
