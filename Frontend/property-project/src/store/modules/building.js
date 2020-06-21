export default {
    actions: {
        // async searchBuildings(ctx, query=''){
        //     const axios = require('axios');
        //     axios.get('http://127.0.0.1:8000/api/buildings/').then(resp => {
        //         const foundBuildings = resp.data;
        //         console.log(foundBuildings)
        //         ctx.commit('updateBuildings', foundBuildings)
        //     })
        // }
        async searchBuildings(ctx, findParams={}){
            const qs = require('qs');
            const axios = require('axios');
            const searchId = qs.stringify(findParams, {arrayFormat: 'repeat'})

            axios.get('http://127.0.0.1:8000/api/buildings?'+ searchId, 
            // {
            //  searchId,
            // paramsSerializer: params => {
            //     // console.log('Find params while searching: ')
            //     // console.log(qs.stringify(params, {arrayFormat: 'repeat'}))  
            //     return qs.stringify(params, {arrayFormat: 'repeat'})
            // }
            // }
            ).then(resp => {
            const foundBuildings = resp.data.results
            const buildingsCount = resp.data.count
            const totalPages = resp.data.total_pages
            const currentPage = resp.data.current
            const nextPageLink = resp.data.next
            const previousPageLink = resp.data.previous
            console.log('FOUND BUILDINGS')
            console.log(foundBuildings)
            ctx.commit('updateBuildings', foundBuildings)
            ctx.commit('updateBuildingsCount', buildingsCount)
            ctx.commit('updateTotalPages', totalPages)
            ctx.commit('updateCurrentPage', currentPage)
            ctx.commit('updateNextPageLink', nextPageLink)
            ctx.commit('updatePreviousPageLink', previousPageLink)
            ctx.commit('updateSearchId', searchId)
            })
        }
    },
    mutations: {
        updateBuildings(state, buildings){
            state.buildings = buildings
        },
        updateBuildingsCount(state, count){
            state.buildingsCount = count
        },
        updateTotalPages(state, totalPages){
            state.totalPages = totalPages
        },
        updateCurrentPage(state, currentPage){
            state.currentPage = currentPage
        },
        updateNextPageLink(state, nextPageLink){
            state.nextPageLink = nextPageLink
        },
        updatePreviousPageLink(state, previousPageLink){
            state.previousPageLink = previousPageLink
        },
        updateSearchId(state, searchId){
            state.searchId = searchId
        }
    },
    state: {
        buildings: [],
        searchId: '',
        buildingsCount: 0,
        totalPages: 0,
        currentPage: 0,
        nextPageLink: null,
        previousPageLink: null,
        // loadedBuildings: [],
        // currentFindParams: {},
    },
    getters: {
        allBuildings(state){
            return state.buildings
        },
        buildingsCount(state){
            return state.buildingsCount
        },
        totalPages(state){
            return state.totalPages
        },
        currentPage(state){
            return state.currentPage
        },
        nextPageLink(state){
            return state.nextPageLink
        },
        previousPageLink(state){
            return state.previousPageLink
        },
        searchId(state){
            return state.searchId
        }
        // getLoadedBuilding(state, slug){
        //     return state.loadedBuildings[]
        // }

    },
}