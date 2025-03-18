export default defineEventHandler(async (event) => {
  const baseUrl = useRuntimeConfig().public.apiBase;
  const cookies = parseCookies(event);
  console.log("dashboard.ts parseCookies", cookies);


  try {
    const data = await $fetch(`${baseUrl}/auth/user-info/`, {
    // const data = await $fetch('http://localhost:8000/api/auth/user-info/', {
      method: 'GET',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        "Cookie": `access_token=${cookies.access_token}; refresh_token=${cookies.refresh_token}`, // ✅ Manually attach cookies
      },
    });

    if (data) {
      console.log('dashboard.ts user data', data);
      return { success: true, 'data': data};
    }
  } catch (error) {
    console.error('dashboard.ts error fetch from /auth/user-info');
    throw createError({ statusCode: 401, message: "dashboard.ts no token" });
  } 
});

