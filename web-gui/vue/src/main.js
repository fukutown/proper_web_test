import Vue from 'vue'
import App from './App.vue'
import router from './router/router'
import store from './store/index'
import axios from 'axios'

// import bootstrap-vue
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
Vue.use(BootstrapVue)

const customAxios = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  headers: {
    'Content-Type': 'application/json',
    // 'X-Requested-With': 'XMLHttpRequest',
    // Authorization: 'Bearer {token}'
  },
  responseType: 'json',
  responseEncoding: 'utf-8'
})

Vue.prototype.$axios = customAxios;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
