import { defineEventHandler, getCookie } from "h3";
import { useRuntimeConfig } from '#imports';

export default defineEventHandler(async (event) => {
  const baseUrl = useRuntimeConfig().public.apiBase;
  // console.log('dashboard.ts event', event);
  console.log("dashboard.ts parseCookies", parseCookies(event));

  const token = getCookie(event, "token");
  console.log('dashboard.ts token', token);
  const user = getCookie(event, "user");
  console.log('dashboard.ts user', user);

  // const csrftoken = useCookie("csrf_token");
  // if (!token || !csrftoken) {
  //   console.error('dashboard.ts no token/csrftoken', token, csrftoken);
  //   throw createError({ statusCode: 401, message: "dashboard.ts no token" });
  // } else {
  //   console.log("dashboard.ts extracted token:", token);
  //   console.log("dashboard.ts extracted csrf_token:", csrftoken);

  try {
    const data = await $fetch(`${baseUrl}/auth/user-info/`, {
    // const data = await $fetch('http://localhost:8000/api/auth/user-info/', {
      method: 'POST',
      body: { token: getCookie(event, "token") },
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
        // 'X-CSRFToken': csrftoken,
      },
    });

    if (data) {
      console.log('dashboard.ts user data', data);
      return { success: true, 'data': data};
    }
  } catch (error) {
    console.error('dashboard.ts error fetch from /auth/user-info');
    return;
    throw createError({ statusCode: 401, message: "dashboard.ts no token" });
  } 
});

