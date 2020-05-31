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
            axios.get('http://127.0.0.1:8000/api/buildings/', {
            params: findParams,
            paramsSerializer: params => {
                console.log('Find PARAMS: ')
                console.log(qs.stringify(params, {arrayFormat: 'repeat'}))  
                return qs.stringify(params, {arrayFormat: 'repeat'})
            }
            }).then(resp => {
            const foundBuildings = resp.data.results
            const buildingsCount = resp.data.count
            console.log('FOUND BUILDINGS')
            console.log(foundBuildings)
            ctx.commit('updateBuildings', foundBuildings)
            ctx.commit('updateBuildingsCount', buildingsCount)
            })
        }
    },
    mutations: {
        updateBuildings(state, buildings){
            state.buildings = buildings
        },
        updateBuildingsCount(state, count){
            state.buildingsCount = count
        }
    },
    state: {
        buildings: [],
        buildingsCount: 0,
        // currentFindParams: {},
    },
    getters: {
        allBuildings(state){
            return state.buildings
        },
        buildingsCount(state){
            return state.buildingsCount
        } 
    },
}