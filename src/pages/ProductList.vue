<template>
  <q-page padding>
    <q-spinner v-if="loading" color="primary" size="3em" />
    <q-banner v-if="error" class="bg-red text-white q-mb-md">
      {{ error }}
    </q-banner>

    <div v-if="!loading && !error" class="row q-col-gutter-md">
      <div v-for="product in products" :key="product.id" class="col-xs-12 col-sm-6 col-md-4">
        <q-card class="my-card">
          <!-- ✅ Image Show -->
          <q-img :src="product.image" ratio="4/3" />

          <q-card-section>
            <div class="text-h6">{{ product.title }}</div>
            <div class="text-subtitle2">{{ product.price }} টাকা</div>
            <div class="text-body2">{{ product.description }}</div>
          </q-card-section>

          <!-- ✅ Video Show -->
          <q-card-section v-if="product.video">
            <video controls style="width: 100%">
              <source :src="product.video" type="video/mp4" />
              আপনার ব্রাউজার ভিডিও ট্যাগ সাপোর্ট করে না।
            </video>
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
  fetchProducts()
})
</script>

<style scoped>
.my-card {
  width: 100%;
}
</style>
