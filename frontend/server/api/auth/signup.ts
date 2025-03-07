import { defineEventHandler, readBody } from 'h3';

export default defineEventHandler(async (event) => {
  const body = await readBody(event);

  const response = await $fetch('http://localhost:8000/api/auth/signup/', {
    method: 'POST',
    body,
  });

  return response;
});
