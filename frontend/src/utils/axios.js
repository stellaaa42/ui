import axios from 'axios';

const apiClient = axios.create({
  baseURL: "http://localhost:8000/api/",
  headers: {
    "Content-Type": "application/json",
    // "X-CSRFToken": getCSRFToken()
  },
  withCredentials: true
});

async function fetchCsrfToken() {
  try {
      const response = await apiClient.get("/csrf/");
      document.cookie = `csrftoken=${response.data.csrfToken}; path=/`;  // Store token in cookie
      apiClient.defaults.headers.common["X-CSRFToken"] = response.data.csrfToken;
  } catch (error) {
      console.error("CSRF token fetch failed:", error);
  }
}

fetchCsrfToken();

export default apiClient;
