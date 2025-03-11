<template>
    <div class="dashboard-container">
      <h1>Welcome, {{ user?.name || "User" }}!</h1>
      <p>Email: {{ user?.email }}</p>
      <p>Role: {{ user?.role }}</p>
  
      <h2>Dashboard Stats</h2>
      <p>Total Orders: {{ dashboardStats?.totalOrders }}</p>
      <p>Pending Messages: {{ dashboardStats?.pendingMessages }}</p>
      <p>Notifications: {{ dashboardStats?.notifications }}</p>

    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";

  const user = ref(null);
  const dashboardStats = ref(null);
  
  onMounted(async () => {
  try {
    const data = await $fetch("/dashboard"); 
    if (data) {
      user.value = data.user;
      dashboardStats.value = data.dashboardStats;
    } else {
      console.error("❌ No data received from /dashboard", error.value);
    }
  } catch (error) {
    console.error("❌ API Error:", error);
  }
  });
  </script>
  
  <style scoped>
  .dashboard-container {
    max-width: 600px;
    margin: auto;
    text-align: center;
  }
  button {
    margin-top: 20px;
    padding: 10px;
    background: red;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
  