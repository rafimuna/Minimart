import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

// ✅ products নামের Pinia store তৈরি করলাম
export const useProductStore = defineStore('products', () => {
  // ✅ products list রাখার জন্য state (reactive data)
  const products = ref([])

  // ✅ loading আর error handle করার জন্য state
  const loading = ref(false)
  const error = ref(null)

  // ✅ function: backend থেকে products fetch করে state-এ বসায়
  const fetchProducts = async () => {
    loading.value = true
    error.value = null

    try {
      const response = await axios.get('http://127.0.0.1:8000/api/products/')
      // ✅ backend থেকে successfully data এলে products-এ সেট করি
      products.value = response.data
    } catch (err) {
      error.value = 'পণ্য লোড করা যায়নি।'
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  // ✅ return করি যেন বাইরে থেকে access করা যায়
  return {
    products,
    loading,
    error,
    fetchProducts,
  }
})
