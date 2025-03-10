import { defineEventHandler, getQuery, setCookie, createError } from "h3";
import { useRuntimeConfig } from "#imports";

// Define OAuth response types
type TokenResponse = {
  access_token: string;
  id_token: string;
  expires_in: number;
  token_type: string;
  scope: string;
};

type UserInfo = {
  email: string;
  name: string;
  picture?: string;
};

export default defineEventHandler(async (event) => {
  const GOOGLE_CLIENT_ID = process.env.GOOGLE_CLIENT_ID;
  const GOOGLE_CLIENT_SECRET = process.env.GOOGLE_CLIENT_SECRET;
  const GOOGLE_REDIRECT_URI = process.env.GOOGLE_REDIRECT_URI || "http://localhost:3000/auth/google";

  if (!GOOGLE_CLIENT_ID || !GOOGLE_CLIENT_SECRET) {
    throw createError({ statusCode: 500, message: "Missing Google OAuth credentials" });
  }

  const googleAuthUrl = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${GOOGLE_CLIENT_ID}&redirect_uri=${GOOGLE_REDIRECT_URI}&response_type=code&scope=email%20profile&access_type=offline&prompt=consent`;

  return { url: googleAuthUrl };
  // try {
  //   // Exchange authorization code for access token
  //   const tokenResponse: TokenResponse = await $fetch("https://oauth2.googleapis.com/token", {
  //     method: "POST",
  //     body: {
  //       client_id: GOOGLE_CLIENT_ID,
  //       client_secret: GOOGLE_CLIENT_SECRET,
  //       redirect_uri: GOOGLE_REDIRECT_URI,
  //       grant_type: "authorization_code",
  //       code,
  //     },
  //   });

  //   // ✅ Now TypeScript knows `access_token` and `id_token` exist
  //   const { access_token, id_token } = tokenResponse;
  //   if (!access_token || !id_token) throw createError({ statusCode: 500, message: "Failed to obtain access token" });

  //   // Fetch user info from Google API
  //   const userInfo: UserInfo = await $fetch("https://www.googleapis.com/oauth2/v3/userinfo", {
  //     headers: { Authorization: `Bearer ${access_token}` },
  //   });

  //   // Securely store the user email in HTTP-only cookie
  //   setCookie(event, "user_email", userInfo.email, {
  //     httpOnly: true,
  //     secure: process.env.NODE_ENV === "production",
  //     path: "/",
  //     maxAge: 60 * 60 * 24 * 7, // 7 days
  //   });

  //   return { email: userInfo.email, name: userInfo.name, picture: userInfo.picture };
  // } catch (err: unknown) {
  //   const errorMessage = err instanceof Error ? err.message : "Unknown error occurred";
  //   throw createError({ statusCode: 500, message: `OAuth error: ${errorMessage}` });
  // }
});
