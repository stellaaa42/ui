import { ref } from "vue";

import { useState } from "nuxt/app";

interface User {
  id: number;
  name: string;
  email: string;
}

export function useAuth() {
  const user = useState<any | null>("user", () => null); // ✅ Explicitly typed user
  const authenticated = useState<boolean>("authenticated", () => false); // ✅ Typed as boolean

  const fetchUser = async () => {
    const response = await useFetch<{ authenticated: boolean; user: any }>("/api/auth/me", {
      credentials: "include",
    });

    authenticated.value = response.data.value?.authenticated ?? false; 
    user.value = response.data.value?.user || null;
    console.log("✅ composables/useAuth.ts fetchUser() - Updated user:", user.value);
  };

  return { user, authenticated, fetchUser };
}