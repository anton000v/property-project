import Vue from 'vue'
import App from './App.vue'
import './assets/css/main.css'
import 'vue-search-select/dist/VueSearchSelect.css'
import store from './store/index.js'
import router from './router/router.js'
import VModal from 'vue-js-modal'
import VueScrollactive from 'vue-scrollactive';
import Axios from 'axios'
import {getAuthToken} from "./backend"

// Env files support
require('dotenv').config()

Vue.prototype.$http = Axios;

// Set token for backend
const token = getAuthToken();
if (token) {
    let prepared_token = `Token ${token}`;
    console.log("Prepared token: ", prepared_token);
    Vue.prototype.$http.defaults.headers.common['Authorization'] = prepared_token
} else {
    console.log("Can't get an api token")
}

console.log(Vue.prototype.$http.defaults.headers.common);


Vue.use(VueScrollactive);

Vue.use(VModal)


Vue.config.productionTip = false


new Vue({
    store: store,
    router: router,
    // router,
    render: h => h(App),
}).$mount('#app')
