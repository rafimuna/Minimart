import { defineStore } from 'pinia'
import { api } from 'boot/axios'
import { ref } from 'vue'

// ✅ 'product' নামে একটা Store বানালাম
export const useProductStore = defineStore('product', () => {
  const products = ref([]) // পণ্যের তালিকা রাখার জন্য
  const loading = ref(false) // লোডিং স্টেট
  const error = ref(null) // যদি কোনো সমস্যা হয়

  // ✅ Backend থেকে Products API call করে ডাটা নিয়ে আসবে
  const fetchProducts = async () => {
    loading.value = true
    error.value = null

    try {
      const response = await api.get('products/products/') // ✅ API endpoint
      products.value = response.data
    } catch (err) {
      error.value = 'পণ্য লোড করা যাচ্ছে না।'
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  return {
    products,
    loading,
    error,
    fetchProducts,
  }
})
