<template>
    <div v-if="showBanner" class="cookie-banner">
      <p>We use cookies to improve your experience. Accept tracking?</p>
      <button @click="acceptCookies">Accept</button>
      <button @click="rejectCookies">Reject</button>
    </div>
  </template>
  
  <script setup>
  import { useCookie } from "#app";
  
  const showBanner = ref(true);
  const trackingConsent = useCookie("tracking_consent");
  
  const acceptCookies = () => {
    trackingConsent.value = "accepted"; // Store consent in a cookie
    showBanner.value = false;
  };
  
  const rejectCookies = () => {
    trackingConsent.value = "rejected"; // Store rejection
    showBanner.value = false;
  };
  </script>
  
  <style>
  .cookie-banner {
    position: fixed;
    bottom: 10px;
    left: 10px;
    background: #222;
    color: #fff;
    padding: 10px;
    border-radius: 5px;
  }
  </style>
  