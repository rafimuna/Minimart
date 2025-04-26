<template>
  <q-page padding>
    <!-- যদি লোডিং হয় তাহলে স্পিনার দেখাবো -->
    <q-spinner v-if="loading" color="primary" size="3em" />

    <!-- যদি Error হয় তাহলে Error Banner দেখাবো -->
    <q-banner v-if="error" class="bg-red text-white q-mb-md">
      {{ error }}
    </q-banner>

    <!-- পণ্য গুলো দেখানোর জন্য কার্ড লিস্ট -->
    <div v-if="!loading && !error" class="row q-col-gutter-md">
      <div v-for="product in products" :key="product.id" class="col-xs-12 col-sm-6 col-md-4">
        <q-card class="my-card">
          <q-img :src="product.image" ratio="4/3" />

          <q-card-section>
            <div class="text-h6">{{ product.title }}</div>
            <div class="text-subtitle2">{{ product.price }} টাকা</div>
          </q-card-section>

          <q-card-actions>
            <q-btn flat label="Add to Cart" color="primary" />
          </q-card-actions>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { onMounted } from 'vue'
import { useProductStore } from 'stores/productStore'

const productStore = useProductStore()
const { fetchProducts, products, loading, error } = productStore

onMounted(() => {
  fetchProducts() // ✅ পেজ লোড হলে Products API থেকে ফেচ করবো
})
</script>

<style scoped>
.my-card {
  width: 100%;
}
</style>
