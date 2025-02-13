import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

const app = createApp(App);
app.use(router);  // Enable Vue Router
app.mount('#app');