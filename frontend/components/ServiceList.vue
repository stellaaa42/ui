<template>
    <div class="service-list">
      <h2>Our Services</h2><br>
      <p v-if="loading">Loading services...</p>
  
      <ul v-if="services.length">
        <li v-for="service in services" :key="service.id">
          {{ service.name }} (€{{ service.price_per_hour }}/hour)
        </li>
      </ul>
  
      <p v-if="!loading && services.length === 0">No services available.</p>
    </div>
  </template>
  
  <script setup>
    import { ref, onMounted } from "vue";
    import { useRuntimeConfig } from "#app";

    const config = useRuntimeConfig(); // ✅ Fetch API base from Nuxt config
    const services = ref([]);
    const loading = ref(true);
    const errorMessage = ref("");

    const fetchServices = async () => {
      loading.value = true;
      errorMessage.value = "";

      // const response = await fetch(`${config.public.apiBase}/services`);
      // const json = await response.json();
      // console.log("🔥 RAW FETCH RESPONSE:", json);
      await new Promise(resolve => setTimeout(resolve, 1000));
      try {
        const { data, error } = await useFetch("/services", {
          method: "GET",
          baseURL: config.public.apiBase, 
        });

        console.log("🌍 API Base URL:", config.public.apiBase);

        if (error.value) {
          errorMessage.value = `No services`;
          console.error("🚨 Fetch error:", error.value);
        } else {
          console.log("📦 Service List:", data.value);
          console.log("stringify List:", JSON.stringify(data.value, null, 2));
          services.value = data.value || []; // Ensure it's always an array
        }
      } catch (err) {
        errorMessage.value = "Unexpected error fetching services.";
        console.error("🔥 Unexpected error:", err);
      } finally {
        loading.value = false;
      }
    };

    // ✅ Fetch services when component is mounted
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