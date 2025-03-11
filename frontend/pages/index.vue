<template>
  <div>
    <div class="hero">
      <div class="content">
        <h1>Premium On-Demand Services</h1>
        <p>Book professional services with ease.</p>
        <div class="buttons">
          <NuxtLink to="/book" no-prefetch class="btn primary">Book Now</NuxtLink>
          <NuxtLink to="/" class="btn secondary">Learn More</NuxtLink>
        </div>
      </div>
    </div>
    <section class="services">
      <ServiceList />
    </section>
    <div class="newsletter-container">
      <div class="newsletter-box">
        <h2 class="newsletter-title">Subscribe to Our Newsletter</h2>
        <p class="newsletter-text">Stay updated with our latest news and offers.</p>

        <form @submit.prevent="subscribe" class="newsletter-form">
          <input
            v-model="email"
            type="email"
            placeholder="Enter your email"
            class="newsletter-input"
            required
          />
          <button type="submit" class="newsletter-button">Subscribe</button>
        </form>

        <p v-if="message" class="newsletter-message">{{ message }}</p>
      </div>
  </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const email = ref("");
const message = ref("");

const subscribe = () => {
  if (!email.value.includes("@")) {
    message.value = "Please enter a valid email address!";
    return;
  }
  // Simulate subscription action (replace with actual API call)
  setTimeout(() => {
    message.value = "Thank you for subscribing!";
    email.value = "";
  }, 1000);
};
</script>

<style scoped>
/* Add any additional styling if needed */
</style>





<style scoped>
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

.loading,
.empty,
.error {
  font-size: 18px;
  margin-top: 20px;
}

.error {
  color: red;
}

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

.newsletter-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
  background: linear-gradient(to right, #1a1a2e, #16213e);
  padding: 40px 20px;
}

/* 📨 Box Styling */
.newsletter-box {
  background: #222;
  color: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  text-align: center;
}

/* 🏆 Title & Text */
.newsletter-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.newsletter-text {
  font-size: 14px;
  color: #b0b0b0;
  margin-bottom: 20px;
}

/* ✍️ Input Field */
.newsletter-input {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: 1px solid #444;
  border-radius: 8px;
  outline: none;
  background: #333;
  color: white;
  margin-bottom: 10px;
}

.newsletter-input::placeholder {
  color: #aaa;
}

/* 🔘 Subscribe Button */
.newsletter-button {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  font-weight: bold;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.newsletter-button:hover {
  background: #0056b3;
}

/* ✅ Subscription Message */
.newsletter-message {
  margin-top: 10px;
  font-size: 14px;
  color: #28a745;
}
</style>