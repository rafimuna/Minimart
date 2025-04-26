import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
  }),
  actions: {
    setUser(payload) {
      this.user = payload
    },
    logout() {
      this.user = null
    },
  },
})
