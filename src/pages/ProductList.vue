<template>
  <q-page padding>
    <q-spinner v-if="loading" color="primary" size="3em" />
    <q-banner v-if="error" class="bg-red text-white">{{ error }}</q-banner>

    <div v-if="!loading && !error" class="row q-col-gutter-md">
      <div v-for="product in products" :key="product.id" class="col-xs-12 col-sm-6 col-md-4">
        <q-card>
          <q-img :src="product.image" ratio="4/3" />
          <q-card-section>
            <div class="text-h6">{{ product.title }}</div>
            <div class="text-subtitle2">{{ product.price }} Taka</div>
          </q-card-section>
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
