import Vue from 'vue'
import App from './App.vue'
import './assets/css/main.css'
import 'vue-search-select/dist/VueSearchSelect.css'
import store from './store/index.js'
import router from './router/router.js'
import VModal from 'vue-js-modal'
import VueScrollactive from 'vue-scrollactive';
import Axios from 'axios'


Vue.prototype.$http = Axios;
const token = 'Token a94b0c7e4c76acfd71bc6e5ce8432a2b787811da'
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}

Vue.use(VueScrollactive);

Vue.use(VModal)


Vue.config.productionTip = false


new Vue({
  store: store,
  router:router,
  // router,
  render: h => h(App),
}).$mount('#app')
