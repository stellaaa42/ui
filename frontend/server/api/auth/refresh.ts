import { defineEventHandler, getCookie } from 'h3';

export default defineEventHandler(async (event) => {
  const refreshToken = getCookie(event, 'refresh_token');

  if (!refreshToken) {
    return { error: 'Refresh token missing' };
  }

  try {
    const response = await $fetch<{ access: string }>(
      'http://localhost:8000/api/auth/refresh/',
      {
        method: 'POST',
        body: { refresh: refreshToken },
      }
    );

    return { access: response.access };
  } catch (error) {
    console.error('Token refresh failed:', error);
    return { error: 'Invalid refresh token' };
  }
});
