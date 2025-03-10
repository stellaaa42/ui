// import { defineEventHandler, readBody, setCookie } from 'h3';

// interface LoginResponse {
//   access: string;
//   user: { name: string };
// }

// export default defineEventHandler(async (event) => {
//   const body = await readBody(event);

//   try {
//     const response = await $fetch<LoginResponse>('http://localhost:8000/api/login/', {
//       method: 'POST',
//       body,
//     });

//     if (response?.access) {
//       setCookie(event, 'access_token', response.access, {
//         httpOnly: true,
//         secure: false, // Change to `true` in production
//         sameSite: 'lax',
//       });
//       return { user: response.user };
//     }

//     return { error: 'Invalid credentials' };
//   } catch (error) {
//     console.error("Login request failed:", error);
//     return { error: 'Failed to authenticate. Please check your credentials and try again.' };
//   }
// });
