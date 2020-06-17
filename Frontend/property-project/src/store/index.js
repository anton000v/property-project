import Vue from 'vue'
import Vuex from 'vuex'
import building from './modules/building'
import buildingsSearchKit from './modules/buildingsSearchKit'
import commonData from './modules/commonData' 
import VueAwesomeSwiper from 'vue-awesome-swiper'

// import style
import 'swiper/css/swiper.css'

// import localStorage from './modules/localStorage'
Vue.use(Vuex)
Vue.use(VueAwesomeSwiper, /* { default options with global component } */)


export default new Vuex.Store({

    modules:{
        building,
        buildingsSearchKit,
        commonData
        // localStorage
    }
})