// src/stores/user.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    isAuthenticated: false,
    user: null,
    token: null,
  }),
  actions: {
    setUser(data) {
      this.user = data.user
      this.token = data.token
      this.isAuthenticated = true
    },
    logout() {
      this.user = null
      this.token = null
      this.isAuthenticated = false
    },
  },
})
