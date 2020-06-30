import Vue from 'vue'
import Router from 'vue-router'
import vSearchPage from '../pages/v-search-page.vue'
import vBuildingPage from '../pages/v-building-page.vue'
import vMapSearchPage from '../pages/v-map-search-page.vue'
import vNotFoundPage from '../pages/v-not-found-page.vue'
import vFlatPage from '../pages/v-flat-page.vue'

Vue.use(Router);

export default new Router({
    // mode: 'history',
    routes:[
        {
            path: '/',
            name: 'home',
            component: vSearchPage,
            // children: [
            //   {
            //   path: '/buildings',
            //   name: 'search-buildings',
            //   component: vSearchPage,
            //   },
            //   {
            //     path: '/flats',
            //     name: 'search-flats',
            //     component: vSearchPage
            //   }
            // ]
        },
        // {
        //     path: '/buildings',
        //     name: 'search-page',
        //     component: vSearchPage,
        //     // props: (route) => ({ findParams: route.query }),
        //     // meta: {
        //     //     showModal: false
        //     // }
        // },
        {
          path: '/buildings',
          name: 'search-buildings',
          component: vSearchPage,
          // children: [
            
          // ]
        },
        {
          path: '/flats',
          name: 'search-flats',
          component: vSearchPage
        },
        {
          path: '/flats/:slug/[:id]',
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
          // children: [
          //   {
          //   path: '/',
          //   name: 'search-page',
          //   component: vSearchPage,
          //   }
          // ]
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