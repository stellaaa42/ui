import { defineEventHandler, deleteCookie } from 'h3';

export default defineEventHandler(async (event) => {
  try {
    // deleteCookie(event, 'token', {
    //   httpOnly: false,
    //   secure: process.env.NODE_ENV === "production",
    //   sameSite: 'None' as any,
    // }

    const body = await readBody(event);
    const apiBase = useRuntimeConfig().public.apiBase;
    const response = await $fetch(`${apiBase}/auth/logout/`, {
      method: 'POST',
      body,
      headers: {
        Cookie: event.req.headers.cookie || "", // Pass client cookies
      },
      credentials: "include",
    });

    return { message: 'logout.ts logged out successfully', response };
  } catch (error) {
    console.error('logout.ts error', error);
    return { error: 'Failed to logout' };
  }
});
