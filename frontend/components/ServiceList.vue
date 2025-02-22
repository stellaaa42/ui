<template>
    <div class="service-list">
      <h2>Our Services</h2>
      <p v-if="loading">Loading services...</p>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  
      <ul v-if="services.length">
        <li v-for="service in services" :key="service.id">
          {{ service.name }} (€{{ service.price_per_hour }}/hour)
        </li>
      </ul>
  
      <p v-if="!loading && services.length === 0">No services available.</p>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
//   import { useRuntimeConfig } from '#app';

  const { $axios } = useNuxtApp();
    // const config = useRuntimeConfig();
  const services = ref([]);
  const loading = ref(true);
  const errorMessage = ref('');
  
  const fetchServices = async () => {
    try {
      const response = await $axios.get('items/');
      console.log('servicelist', response);
    //   const response = await $fetch(`${config.public.apiBase}items/`);
      services.value = response.data;
    } catch (error) {
      errorMessage.value = 'Error fetching services.';
      console.error('Error fetching services:', error);
    } finally {
      loading.value = false;
    }
  };
  
  // ✅ Triggers fetch after component is mounted
  onMounted(() => {
    fetchServices();
  });
  </script>
  
  <style scoped>
  .service-list {
    padding: 20px;
    background-color: #f8f9fa;
    border-radius: 8px;
    max-width: 600px;
    margin: 20px auto;
  }
  
  .service-list h2 {
    text-align: center;
    margin-bottom: 10px;
  }
  
  .service-list ul {
    list-style-type: none;
    padding: 0;
  }
  
  .service-list li {
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  .service-list li:last-child {
    border-bottom: none;
  }

  .error {
  color: red;
  text-align: center;
  }
  </style>