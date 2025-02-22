<template>
  <div>
    <div class="hero">
      <div class="content">
        <h1>Premium On-Demand Services</h1>
        <p>Book professional services with ease.</p>
        <div class="buttons">
          <NuxtLink to="/book" class="btn primary">Book Now</NuxtLink>
          <NuxtLink to="/" class="btn secondary">Learn More</NuxtLink>
        </div>
      </div>
    </div>
  <section class="services">
      <h2>Our Services</h2>
      <p v-if="loading">Loading services...</p>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>

      <ul v-if="services.length">
        <li v-for="service in services" :key="service.id">
          {{ service.name }} (€{{ service.price_per_hour }}/hour)
        </li>
      </ul>

      <p v-if="!loading && services.length === 0">No services available.</p>
    </section>
  </div>
</template>

<script setup>
import { useFetch } from '#app';
import { ref } from 'vue';

// Fetch services using useFetch
const { data: servicesData, pending, error } = await useFetch('/items/');

const services = ref(servicesData.value || []);

if (error.value) {
  console.error("Error fetching services:", error.value);
}
</script>

<style>
.hero {
  position: relative;
  width: 100%;
  height: 100vh;
  background: url("@/assets/service1.png") center/cover no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: white;
}

.content {
  max-width: 600px;
}

h1 {
  font-size: 48px;
  font-weight: bold;
}

p {
  font-size: 20px;
  margin: 10px 0 30px;
}

.buttons {
  display: flex;
  gap: 20px;
}

.btn {
  padding: 12px 24px;
  font-size: 18px;
  font-weight: bold;
  border-radius: 5px;
  text-decoration: none;
  transition: background 0.3s ease-in-out;
}

.primary {
  background: #0056ff;
  color: white;
}

.primary:hover {
  background: #0041c4;
}

.secondary {
  background: white;
  color: black;
  border: 1px solid white;
}

.secondary:hover {
  background: rgba(255, 255, 255, 0.8);
}

.services {
  text-align: center;
  padding: 60px 20px;
  background: #f8f9fa;
}

h2 {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 30px;
}

/* Loading & Error Messages */
.loading,
.empty,
.error {
  font-size: 18px;
  margin-top: 20px;
}

.error {
  color: red;
}

/* Service List */
.service-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.service-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
  width: 280px;
  text-align: center;
}

.service-card:hover {
  transform: translateY(-5px);
}

.service-card h3 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.price {
  font-size: 20px;
  font-weight: bold;
  color: #0056ff;
}

</style>

