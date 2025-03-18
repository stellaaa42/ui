<template>
    <div v-if="user" class="dashboard-container">
      <h1>Welcome, {{ user?.name || "User" }}!</h1>
      <!-- <p>Email: {{ user?.email }}</p>
      <p>Role: {{ user?.role }}</p> -->
  
      <h2>Dashboard Stats</h2>
      <p v-if="dashboardStats">Stats: {{ dashboardStats }}</p>
      <!-- <p>Total Orders: {{ dashboardStats?.totalOrders }}</p>
      <p>Pending Messages: {{ dashboardStats?.pendingMessages }}</p>
      <p>Notifications: {{ dashboardStats?.notifications }}</p> -->
    </div>
    <div v-else>
    <p>NO USER, Loading dashboard...</p>
    </div>
  </template>
  
  <script setup>
  import { useAuth } from "@/composables/useAuth";

  const dashboardStats = ref(null);

  const { user, fetchUser } = useAuth();
  console.log("dashboard.vue user:", user.value);

  // definePageMeta({
  //   middleware: "auth",
  // });
  
  onMounted(async () => {
  try {
    if (!user.value) {
      await fetchUser();
    }

    const data = await $fetch("/api/dashboard", {
      method: "GET",
      credentials: "include",
    });

    
    if (data) {
      console.log("dashboard.vue data:", data);
      dashboardStats.value = data.dashboardStats;
    } else {
      console.error("Dashboard.vue No data received from /dashboard.ts", error);
    }
  } catch (error) {
    console.error("❌ Dashboard.vue error");
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
  