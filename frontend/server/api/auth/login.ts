import { defineEventHandler, readBody, setCookie } from 'h3';

const config = useRuntimeConfig();

interface LoginResponse {
  access: string;
  user: { name: string };
}

export default defineEventHandler(async (event) => {
  const body = await readBody(event);

  try {
    const response = await $fetch<LoginResponse>(`${config.public.apiBase}/auth/login/`, {
      method: 'POST',
      body: await readBody(event),
    });

    console.log("Login response:", response);
    if (response?.access) {
      setCookie(event, 'access_token', response.access, {
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        sameSite: 'lax',
        path: "/",
        maxAge: 3600,
      });
      return { response };
    }

    return { error: 'Invalid credentials' };
  } catch (error) {
    console.error("Login request failed:", error);
    return { error: 'Failed to authenticate. Please check your credentials and try again.' };
  }
});
