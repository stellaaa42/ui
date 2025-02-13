<template>
  <div class="hero">
    <div class="content">
      <h1>Premium On-Demand Services</h1>
      <p>Book professional services with ease.</p>
      <div class="buttons">
        <router-link to="/book" class="btn primary">Book Now</router-link>
        <router-link to="/services" class="btn secondary">Learn More</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage"
};
</script>

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
</style>
