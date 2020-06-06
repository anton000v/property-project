import Vue from 'vue'
import Vuex from 'vuex'
import building from './modules/building'
import buildingsSearchKit from './modules/buildingsSearchKit'
// import localStorage from './modules/localStorage'
Vue.use(Vuex)

export default new Vuex.Store({

    modules:{
        building,
        buildingsSearchKit,
        // localStorage
    }
})