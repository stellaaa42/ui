


export default defineEventHandler(async (event) => {
    if (event.node.req.method === "GET") {
      return { error: "This endpoint only supports POST requests." }; // ✅ Instead of throwing 405
    }
  
    if (event.node.req.method !== "POST") {
      throw createError({ statusCode: 405, message: "Method Not Allowed" });
    }
  
    const body = await readBody(event);
    return { message: "Booking successful!", data: body };
  });