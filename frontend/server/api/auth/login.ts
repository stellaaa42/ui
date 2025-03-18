import { defineEventHandler, readBody, setCookie } from 'h3';

const config = useRuntimeConfig();

interface LoginResponse {
  user: any;
  access_token: string;
  refresh: string;
}

export default defineEventHandler(async (event) => {
  try {
    const body = await readBody(event);
    const response = await $fetch<LoginResponse>(`${config.public.apiBase}/auth/login/`, {
      method: 'POST',
      body: body,
      credentials: "include",
    });

    console.log("login.ts response:", response);

    if (response?.access_token && response?.refresh) {

      setCookie(event, "access_token", response.access_token, {
        httpOnly: true, // Prevent JavaScript access (XSS protection)
        secure: process.env.NODE_ENV === "production", // Enable in production
        sameSite: "lax", // Allow cookie for same-site requests
        path: "/",
        maxAge: 300, // 5 minutes
      });

      // Set Refresh Token in HTTP-Only Cookie (long lifespan)
      setCookie(event, "refresh", response.refresh, {
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        sameSite: "lax",
        path: "/",
        maxAge: 604800, // 7 days
      });

      console.log("login.ts response.user:", response.user);
      return { success: true, user: response.user };
    }

    console.error("No response:", response);
    return { success: false, error: "No response." };
  } catch (error) {
    console.error("Login request failed:", error);
    return { error: 'Your usename or password might not be correct' };
  }
});
