import axios from 'axios';

export default defineNuxtPlugin((nuxtApp) => {

  const axiosInstance = axios.create({
    baseURL: 'http://localhost:8000/api/', // Set base URL
    withCredentials: true,                 // Enable cookies for CORS
    headers: {
      'Content-Type': 'application/json'
    }
  });

  // Fetch CSRF Token and set it in cookies & headers
  const fetchCsrfToken = async () => {
    try {
      const response = await axiosInstance.get('/csrf/');
      const csrfToken = response.data.csrfToken;

      const csrfCookie = useCookie('csrftoken');
      csrfCookie.value = csrfToken;

      axiosInstance.defaults.headers['X-CSRFToken'] = csrfToken;

    } catch (error) {
      console.error('CSRF token fetch failed:', error);
    }
  };

  // Call CSRF fetch on plugin initialization
  fetchCsrfToken();

  // Global Axios error handling
  axiosInstance.interceptors.response.use(
    (response) => response, // ✅ Typed response
    (error) => { 
      if (error.response && error.response.status === 401) {
        console.error('Unauthorized. Redirecting to login...');
        useRouter().push('/login'); // Use Nuxt Router for redirection
      }
      return Promise.reject(error);
    }
  );

  // Provide Axios instance globally in the app
  nuxtApp.provide('axios', axiosInstance);
});
