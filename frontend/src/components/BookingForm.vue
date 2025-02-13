<template>
    <form @submit.prevent="submitBooking" class="booking-form">
      <input v-model="booking.name" placeholder="Your Name" required /><br>
      <input v-model="booking.email" type="email" placeholder="Your Email" required /><br>
      <textarea v-model="booking.address" placeholder="Your Address" required></textarea><br>
  
      <label>Select Service:</label>
      <select v-model="booking.service">
        <option value="standard">Standard (€35/hour)</option>
        <option value="deep">Deep (€55/hour)</option>
        <option value="custom">Custom Service (Price Varies)</option>
      </select><br>
  
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
    </form>
  </template>
  
  <script>
  import apiClient from "@/utils/axios.js";
  
  export default {
    data() {
      return {
        booking: {
          name: '',
          email: '',
          address: '',
          service: 'standard',
          appointment_date: '',
          appointment_time: '',
          payment_method: '',
          card_number: '',
          card_cvv: '',
          card_expiration: ''
        }
      };
    },
    methods: {
      async submitBooking() {
        try {
            await apiClient.post("book/", this.booking);
        //   const response = await apiClient.post("book/", this.booking);
          alert("Booking Successful!");
        } catch (error) {
          alert("Error submitting booking: " + error);
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
  