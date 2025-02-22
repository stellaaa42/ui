<template>
    <form @submit.prevent="submitBooking" class="booking-form">
      <input v-model="booking.name" placeholder="Your Name" required /><br>
      <input v-model="booking.email" type="email" placeholder="Your Email" required /><br>
      <textarea v-model="booking.address" placeholder="Your Address" required></textarea><br>
  
      <div>
        <label>Select A Service:</label>
        <select v-model="booking.service">
          <option disabled value="">Select a service</option>
          <option v-for="service in services" :key="service.id" :value="service.id">
            {{ service.name }} (€{{ service.price_per_hour }}/hour)
          </option>
        </select>
  
        <p v-if="loading">Loading services...</p>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        <p v-if="services.length === 0 && !loading">No services found.</p>
  
        <label>Select Area:</label>
        <select v-model="booking.area">
          <option disabled value="">Select An Area</option>
          <option v-for="area in areas" :key="area.id" :value="area.id">
            {{ area.name }} ({{ area.description }})
          </option>
        </select>
        <p v-if="loadingAreas">Loading areas...</p>
        <p v-if="areaError" class="error">{{ areaError }}</p>
        <p v-if="areas.length === 0 && !loadingAreas">No areas found.</p>
      </div>
  
      <input v-model="booking.appointment_date" type="date" required /><br>
      <input v-model="booking.appointment_time" type="time" required /><br>
  
      <label>Select Payment Method:</label>
      <select v-model="booking.payment_method">
        <option value="card">Credit/Debit Card</option>
        <option value="paypal">PayPal</option>
      </select><br>
  
      <div v-if="booking.payment_method === 'card'">
        <input v-model="booking.card_number" type="text" maxlength="16" placeholder="Card Number" required /><br>
        <input v-model="booking.card_cvv" type="text" maxlength="3" placeholder="CVV" required /><br>
        <input v-model="booking.card_expiration" type="text" placeholder="MM/YYYY" required /><br>
      </div>
  
      <button type="submit">Submit Booking</button>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </form>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';

  
  // Reactive state variables
  const services = ref([]);
  const areas = ref([]);
  const loading = ref(false);
  const loadingAreas = ref(false);
  const errorMessage = ref('');
  const areaError = ref('');
  
  const booking = ref({
    name: '',
    email: '',
    address: '',
    service: '',
    area: '',
    appointment_date: '',
    appointment_time: '',
    payment_method: '',
    card_number: '',
    card_cvv: '',
    card_expiration: ''
  });
  
  // Fetch Services
  const fetchServices = async () => {
    loading.value = true;
    errorMessage.value = '';
    try {
      const response = await $axios.get('http://localhost:8000/api/items/');
      services.value = response.data;
    } catch (error) {
      errorMessage.value = 'Failed to load services.';
      console.error("Service fetch error:", error);
    } finally {
      loading.value = false;
    }
  };
  
  // Fetch Areas
  const fetchAreas = async () => {
    loadingAreas.value = true;
    areaError.value = '';
    try {
      const response = await $axios.get('http://localhost:8000/api/areas/');
      areas.value = response.data;
    } catch (error) {
      areaError.value = 'Failed to load areas. Please try again.';
      console.error("Area fetch error:", error);
    } finally {
      loadingAreas.value = false;
    }
  };
  
  // Submit Booking
  const submitBooking = async () => {
    try {
      const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1] || "";
      const response = await $axios.post('book/', booking.value, {
        headers: {
          'X-CSRFToken': csrfToken,
        },
        withCredentials: true
      });
      console.log("Booking successful:", response.data);
      alert("Booking Successful!");
    } catch (error) {
      console.error("Booking error:", error.response?.data || error);
      errorMessage.value = "Error submitting booking. Please check your details.";
      alert("Error submitting booking: " + (error.response ? JSON.stringify(error.response.data) : error));
    }
  };
  
  // Run on page load
  onMounted(() => {
    fetchServices();
    fetchAreas();
  });
  </script>
  
  <style scoped>
  .booking-form {
    background: white;
    padding: 30px;
    border-radius: 8px;
    width: 350px;
    margin: 0 auto;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  input, select, textarea {
    width: 100%;
    margin-bottom: 12px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  button {
    background: #0056ff;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 5px;
    font-weight: bold;
    cursor: pointer;
  }
  
  button:hover {
    background: #0041c4;
  }
  
  .error {
    color: red;
    font-size: 0.9em;
  }
  </style>
  