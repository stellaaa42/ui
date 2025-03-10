// import { useCookie } from '#app';

// export function useAuth() {
//   const user = useCookie('user', { default: () => null });
//   const isAuthenticated = computed(() => !!user.value);

//   async function login(username: string, password: string) {
//     const config = useRuntimeConfig();
//     const { data, error } = await useFetch<{ user: any } | null>(
//       `${config.public.apiBase}/auth/login`, 
//       {
//       method: 'POST',
//       body: { username, password },
//     });

//     if (data.value && !error.value) {
//       user.value = data.value.user;
//       navigateTo("/dashboard");
//       return { success: true };
//     }

//     return { success: false, message: error.value?.message || "Login failed" };
//   }

//   async function signup(username: string, password: string) {
//     const config = useRuntimeConfig();
//     const { data, error } = await useFetch<{ message: string } | null>(
//       `${config.public.apiBase}/auth/signup`, 
//       {
//       method: 'POST',
//       body: { username, password },
//     });

//     if (data.value && !error.value) {
//       return { success: true, message: data.value.message };
//     }

//     return { success: false, message: error.value?.message || "Signup failed" };
//   }

//   async function loginWithOAuth(provider: string) {
//     const config = useRuntimeConfig();
//     const { data, error } = await useFetch<{ user: any } | null>(
//       `${config.public.apiBase}/auth/oauth/${provider}`, {
//       method: 'GET',
//     });

//     if (data.value && !error.value) {
//       user.value = data.value.user;
//       navigateTo("/dashboard");
//       return { success: true };
//     }

//     return { success: false, message: error.value?.message || "OAuth login failed" };
//   }

//   async function logout() {
//     const config = useRuntimeConfig();
//     await useFetch(
//       `${config.public.apiBase}/auth/logout`, { 
//         method: 'POST' 
//       });
//     user.value = null;
//     navigateTo("/");
//   }

//   return { user, isAuthenticated, login, signup, loginWithOAuth, logout };
// }
