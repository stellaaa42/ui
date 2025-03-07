import { defineEventHandler, getQuery } from 'h3';

export default defineEventHandler(async (event) => {
  const { provider } = getQuery(event); // e.g., 'google' or 'github'

  if (!provider) {
    return { error: 'Missing provider' };
  }

  const response = await $fetch(`http://localhost:8000/api/auth/oauth/${provider}/`, {
    method: 'GET',
  });

  return response;
});
