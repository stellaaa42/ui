import { defineEventHandler, getCookie } from "h3";

export default defineEventHandler(async (event) => {
  console.log("📩 API Hit: /api/dashboard");

  const accessToken = getCookie(event, "access_token");

  if (!accessToken) {
    console.warn("⛔ No token! Unauthorized request.");
    throw createError({ statusCode: 401, message: "Unauthorized" });
  }

  console.log("✅ Token found! Fetching dashboard data...");

  // Simulating user data (Replace this with an actual database/API call)
  return {
    user: {
      name: "John Doe",
      email: "johndoe@example.com",
      role: "Admin",
    },
    dashboardStats: {
      totalOrders: 42,
      pendingMessages: 3,
      notifications: 5,
    },
  };
});
