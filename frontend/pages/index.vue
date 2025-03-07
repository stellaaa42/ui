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
  </div>
</template>

<script>
const config = useRuntimeConfig();
console.log("🌍 API Base:", config.public.apiBase);

const { data, error } = await useFetch(`${config.public.apiBase}/book`, {
  method: "POST",
  body: { username: "test1" },
});

console.log("📡 API Response:", data.value);
console.error("❌ API Error:", error.value);
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
</style>