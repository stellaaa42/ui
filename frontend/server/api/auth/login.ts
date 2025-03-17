import { defineEventHandler, readBody, setCookie } from 'h3';

const config = useRuntimeConfig();

interface LoginResponse {
  access_token: string;
  user: { name: string };
  csrf_token: string;
}

export default defineEventHandler(async (event) => {
  try {
    const response = await $fetch<LoginResponse>(`${config.public.apiBase}/auth/login/`, {
      method: 'POST',
      body: await readBody(event),
    });

    console.log("login.ts response:", response);
    
    if (response?.access_token) {
      setCookie(event, 'token', response.access_token, {
        httpOnly: false,
        // httpOnly: true, // for production
        secure: process.env.NODE_ENV === "production",
        // sameSite: 'lax', // for production
        sameSite: 'None' as any,
        path: "/",
        // maxAge: 3600, // 1 hour
        maxAge: 300, // 5 minutes
      });
      // console.log('login.ts event', event); 

      console.log("login.ts access_token", response.user, response.access_token);
      return { success: true, user: response.user, token: response.access_token};
    }

    console.error("No response:", response);
    return { success: false, error: "No response." };
  } catch (error) {
    console.error("Login request failed:", error);
    return { error: 'Your usename or password might not be correct' };
  }
});
