<template>
  <div>
    <header>
      <Navbar />
    </header>
  </div>
  <main>
      <slot /> <!-- This will render page content -->
  </main>
</template>

<style scoped>
header {
  background-color: #f5f5f5;
  padding: 10px;
  text-align: center;
}
</style>


<script setup>
import Navbar from "~/components/NavBar.vue";
import { useCookie } from "#app";

const trackingConsent = useCookie("tracking_consent");
const trackingData = useCookie("tracking_data", { default: () => [] });
const startTime = ref(Date.now());

setInterval(async () => {
  if (trackingConsent.value === "accepted") {
    await $fetch("/api/tracking", {
      method: "POST",
      body: trackingData.value,
    });

    trackingData.value = []; // Clear stored data after sending
  }
}, 5000);


onMounted(() => {
  if (trackingConsent.value === "accepted") {
    // Track clicks
    document.addEventListener("click", (e) => {
      trackingData.value.push({ type: "click", x: e.clientX, y: e.clientY, time: Date.now() });
    });

    // Track mouse movement
    document.addEventListener("mousemove", (e) => {
      trackingData.value.push({ type: "move", x: e.clientX, y: e.clientY, time: Date.now() });
    });

    // Track time spent on page
    window.addEventListener("beforeunload", () => {
      const timeSpent = Date.now() - startTime.value;
      trackingData.value.push({ type: "stay_time", duration: timeSpent });
    });
  }
});
</script>
