<template>
  <NavBarComponent />
  <router-view />
</template>

<script>
import NavBarComponent from './components/NavBarComponent.vue';

export default {
  components: {
    NavBarComponent
  }
}
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
</style>
