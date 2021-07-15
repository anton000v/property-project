import Vue from 'vue'
import Router from 'vue-router'
// import vSearchPage from '../pages/v-search-page.vue'
import vBuildingPage from '../pages/v-building-page.vue'
import vMapSearchPage from '../pages/v-map-search-page.vue'
import vNotFoundPage from '../pages/v-not-found-page.vue'
import vFlatPage from '../pages/v-flat-page.vue'
import vBuildingsSearchPage from '../pages/v-search-buildings-page.vue'
import vFlatsSearchPage from '../pages/v-search-flats-page.vue'
import vMainPage from '../pages/v-main.page.vue'
Vue.use(Router);

export default new Router({
    mode: 'history',
    routes:[
        {
            path: '/',
            name: 'home',
            component: vMainPage,
        },
        {
          path: '/buildings',
          name: 'search-buildings',
          component: vBuildingsSearchPage,
        },
        {
          path: '/flats',
          name: 'search-flats',
          component: vFlatsSearchPage
        },
        {
          path: '/flats/:slug/:id',
          name: 'flat-page',
          component: vFlatPage
        },
        {
            path: '/buildings/:slug',
            name: 'building-page',
            component: vBuildingPage,
        },
        {
          path: '/map-search',
          name: 'map-search',
          component: vMapSearchPage,
        },
        { path: '*', name:'page-404', component: vNotFoundPage }
    ],
    scrollBehavior (to, from, savedPosition) {
        if (savedPosition) {
          return savedPosition
        } else {
          return { x: 0, y: 0 }
        }
      }
})

// export default router;