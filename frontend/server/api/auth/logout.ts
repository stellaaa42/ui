import { defineEventHandler, deleteCookie } from 'h3';

export default defineEventHandler(async (event) => {
  deleteCookie(event, 'access_token'); // Removes JWT token

  return { message: 'Logged out successfully' };
});
