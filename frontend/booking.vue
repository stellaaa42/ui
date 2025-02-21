<template>
    <div>
      <h1>Book a Service</h1>
        <BookingForm />
    </div>
  </template>
  
  <script>
  import BookingForm from "../components/BookingForm.vue"

  export default {
    components: { BookingForm }
  };
  </script>

<style scoped>
.booking-container {
  text-align: center;
  padding: 80px 20px;
}
</style>
  
  