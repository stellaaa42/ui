import axios from 'axios';

export default defineNuxtPlugin(nuxtApp => {
  const axiosInstance = axios.create({
    baseURL: 'http://localhost:8000/api/',
  });

  nuxtApp.provide('axios', axiosInstance);
});
