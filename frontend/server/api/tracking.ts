import { readBody } from "h3";

export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  
  console.log("Tracking Data Received:", body);
  
  return { status: "success" };
});
