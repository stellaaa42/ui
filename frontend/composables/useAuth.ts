import { useState } from "nuxt/app";

export const useAuth = () => {
  const isAuthenticated = useState<boolean>("isAuthenticated", () => false); // ✅ Persistent state

  const login = () => {
    isAuthenticated.value = true;  // ✅ Automatically updates all components
  };

  const logout = () => {
    isAuthenticated.value = false; // ✅ Updates all components when logging out
  };

  return { isAuthenticated, login, logout };
};
