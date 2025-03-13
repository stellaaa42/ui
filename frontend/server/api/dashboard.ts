import { defineEventHandler, getCookie } from "h3";


export default defineEventHandler(async (event) => {
  const token = getCookie(event, "token");
  const sessionid = getCookie(event, "sessionid");
  console.log("🔍 dashboard.ts parse Cookies in API Request:", parseCookies(event));
  console.log('dashboard.ts sessionid', sessionid);

  if (!token) {
    console.warn("dashboard.ts No token!");
    throw createError({ statusCode: 401, message: "Unauthorized" });
  }

  return { success: true, sessionid };
});
