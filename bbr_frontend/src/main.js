import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import Vue3EasyDataTable from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';

axios.defaults.baseURL = import.meta.env.VITE_API_URL

const app = createApp(App)

app.use(createPinia())
app.use(router, axios)
app.component('VueDatePicker', VueDatePicker)
app.component('EasyDataTable', Vue3EasyDataTable)

app.mount('#app')
