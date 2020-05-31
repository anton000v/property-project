import { baseApiAddress } from '../variables.js';

export default {
    actions: {
        async getSaltovkaSevernayaSaltovkaDBValues(ctx){
            const axios = require('axios');
            axios.get(baseApiAddress + 'get-saltovka-severnaya-saltovka-db-values/').then(resp => {
                const saltovkaDBValue = resp.data[this.saltovkaDBKey];
                const severnayaSaltovkaDBValue = resp.data[this.severnayaSaltovkaDBKey];
                ctx.commit('updateSaltovkaDbValue', saltovkaDBValue)
                ctx.commit('updateSevernayaSaltovkaDbValue', severnayaSaltovkaDBValue)
            })
        }
    },
    mutations: {
        updateSaltovkaDbValue(state, value){
            state.saltovkaDBValue = value
        },
        updateSevernayaSaltovkaDbValue(state, value){
            state.severnayaSaltovkaDBValue = value
        }
    },
    state: {
        saltovkaDBValue: '',
        severnayaSaltovkaDBValue: '',
    },
    getters: {
        saltovkaDBValue(state){
            return state.saltovkaDBValue
        },
        severnayaSaltovkaDBValue(state){
            return state.severnayaSaltovkaDBValue
        }
    },
}