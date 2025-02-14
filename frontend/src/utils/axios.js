import axios from 'axios';

const apiClient = axios.create({
  baseURL: "http://localhost:8000/api/",
  headers: {
    "Content-Type": "application/json",
    // "X-CSRFToken": getCSRFToken()
  },
  withCredentials: true
});

// function getCSRFToken() {
//   const cookie = document.cookie.split("; ").find(row => row.startsWith("csrftoken="));
//   return cookie ? cookie.split("=")[1] : "";
// }

export default apiClient;
