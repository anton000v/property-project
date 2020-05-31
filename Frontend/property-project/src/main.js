import Vue from 'vue'
import App from './App.vue'
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// import '@/assets/css/main.css'
import './assets/css/main.css'
import 'vue-search-select/dist/VueSearchSelect.css'
import store from './store/index.js'

// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// import router from './router'

// Install BootstrapVue
// Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
// Vue.use(IconsPlugin)

Vue.config.productionTip = false
// console.log(App);
new Vue({
  store: store,
  // router,
  render: h => h(App),
}).$mount('#app')
