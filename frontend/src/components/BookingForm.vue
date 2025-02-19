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
  
  <script>
  import apiClient from "@/utils/axios.js";
  
  export default {
    data() {
      return {
        services: [],
        areas: [],
        booking: {
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
        },
        loading:false,
        errorMessage: '',
        loadingAreas: false,
        areaError: ''

      };
    },

    async mounted() {
      this.fetchServices();
      this.fetchAreas();
    },

    methods: {
      async fetchServices() {
        this.loading = true;
        this.errorMessage = null;
        try {
          const response = await apiClient.get("items/"); 
          console.log("form_page Fetched services:", response.data);
          this.services = response.data;
          console.log("form_page Updated services (Vue):", this.services);
        } catch (error) {
          console.error("Error fetching services:", error);
          this.errorMessage = "Failed to load services.";
        } finally {
          this.loading = false;
        }
      },

      async fetchAreas() {
        this.loadingAreas = true;
        this.areaError = null;
      try {
        const response = await apiClient.get("areas/");
        console.log("form_page Fetched areas:", response.data);
        this.areas = response.data;
        console.log("form_page Updated services (Vue):", this.areas);
      } catch (error) {
        this.areaError = "Failed to load areas. Please try again.";
        console.error("Area fetch error:", error);
      } finally {
        this.loadingAreas = false;
      }
    },
      
      async submitBooking() {
        console.log("Submitting Booking:", this.booking);  // ✅ Log the request data
        
        try {
          const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1] || "";

          const response = await apiClient.post("book/", this.booking, {
            headers: {
              "X-CSRFToken": csrfToken,  // ✅ Include CSRF token
            },
            withCredentials: true,
          });
            
          console.log("Success:", response.data);
          alert("Booking Successful!");
        } catch (error) {
          console.error("Error submitting booking:", error.response ? error.response.data : error);
          this.errorMessage = "Error submitting booking. Please check your details.";
          alert("Error submitting booking: " + (error.response ? JSON.stringify(error.response.data) : error));
        }
      }
    }
  };
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
  </style>
  