import Vue from 'vue'
import Router from 'vue-router'
import vSearchPage from '../pages/v-search-page.vue'
import vBuildingPage from '../pages/v-building-page.vue'
import vNotFoundPage from '../pages/v-not-found-page.vue'
Vue.use(Router);

export default new Router({
    // mode: 'history',
    routes:[
        {
            path: '/',
            name: 'home',
            component: vSearchPage,
        },
        {
            path: '/buildings',
            name: 'search-page',
            component: vSearchPage,
            // props: (route) => ({ findParams: route.query }),
            // meta: {
            //     showModal: false
            // }
        },
        {
            path: '/buildings/:slug',
            // props: true,
            name: 'building-page',
            component: vBuildingPage,
            // meta: { transitionName: 'zoom' },
        },
        { path: '*', name:'page-404',component: vNotFoundPage }
    ]
})

// export default router;