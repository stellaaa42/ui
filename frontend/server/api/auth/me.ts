import { defineEventHandler, getCookie } from "h3";

export default defineEventHandler(async (event) => {
  const accessToken = getCookie(event, "access_token");
  const apiBase = useRuntimeConfig().public.apiBase;

  if (!accessToken) {
    return { authenticated: false, user: null };
  }

  try {
    const user = await $fetch(`${apiBase}/auth/user-info/`, {
      method: "GET",
      headers: { Authorization: `Bearer ${accessToken}` },
      credentials: "include",
    });

    return { authenticated: true, user };
  } catch (error) {
    return { authenticated: false, user: null };
  }
});
