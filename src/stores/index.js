// src/stores/index.js
import { createPinia } from 'pinia'

export default function (app) {
  app.use(createPinia())
}
