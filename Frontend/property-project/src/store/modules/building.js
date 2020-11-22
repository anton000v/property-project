import { buildingsBaseVariables } from '../../variables'


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

        async mapSearchBuildings(ctx, findParams={}){

            const qs = require('qs');
            // const axios = require('axios');
            let mapSearchId = qs.stringify(findParams, {arrayFormat: 'repeat'})
            // ctx.commit('updateSearchId', searchId)
            if(mapSearchId.length == 0){
                mapSearchId = 'no_page'
            }
            else{
                mapSearchId += '&no_page'
            }
            this._vm.$http.get(`${buildingsBaseVariables.fullApiAddress}?${mapSearchId}`).then(resp => {
                const foundBuildings = resp.data
                console.log('FOUND BUILDINGS')
                console.log(foundBuildings)

                ctx.commit('updateBuildings', foundBuildings)
            })


        },

        async searchBuildings(ctx, findParams={}){
            const qs = require('qs');
            // const axios = require('axios');
            const searchId = qs.stringify(findParams, {arrayFormat: 'repeat'})
            this._vm.$http.get(`${buildingsBaseVariables.fullApiAddress}?${searchId}`,
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
                const buildingsTotalPages = resp.data.total_pages
                const currentBuildingPage = resp.data.current
                const nextPageLink = resp.data.next
                const previousPageLink = resp.data.previous
                // const perPage = resp.data.per_page
                console.log('FOUND BUILDINGS')
                console.log(foundBuildings)
                ctx.commit('updateBuildings', foundBuildings)
                ctx.commit('updateBuildingsCount', buildingsCount)
                ctx.commit('updateBuildingsTotalPages', buildingsTotalPages)
                ctx.commit('updateCurrentBuildingPage', currentBuildingPage)
                ctx.commit('updateNextPageLink', nextPageLink)
                ctx.commit('updatePreviousPageLink', previousPageLink)
                ctx.commit('updateSearchId', searchId)
                // ctx.commit('updatePerPage', perPage)
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
        updateBuildingsTotalPages(state, buildingsTotalPages){
            state.buildingsTotalPages = buildingsTotalPages
        },
        updateCurrentBuildingPage(state, currentBuildingPage){
            state.currentBuildingPage = currentBuildingPage
        },
        updateNextPageLink(state, nextPageLink){
            state.nextPageLink = nextPageLink
        },
        updatePreviousPageLink(state, previousPageLink){
            state.previousPageLink = previousPageLink
        },
        updateSearchId(state, searchId){
            state.searchId = searchId
        },

        // updatePerPage(state, value){
        //     state.perPage = value
        // }
    },
    state: {
        buildings: [],
        buildingsOnMap: [],
        searchId: '',
        buildingsCount: 0,
        buildingsTotalPages: 0,
        currentBuildingPage: 0,
        nextPageLink: null,
        previousPageLink: null,
 
        // perPage: 0,
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
        buildingsTotalPages(state){
            return state.buildingsTotalPages
        },
        currentBuildingPage(state){
            return state.currentBuildingPage
            
        },
        nextPageLink(state){
            return state.nextPageLink
        },
        previousPageLink(state){
            return state.previousPageLink
        },
        searchId(state){
            return state.searchId
        },

        // elementsPerPage(state){
        //     return state.perPage
        // }
        // getLoadedBuilding(state, slug){
        //     return state.loadedBuildings[]
        // }

    },
}