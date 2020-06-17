
export default {
    mutations: {
       changeMainHeader(state, value){
           state.mainHeader = Boolean(value)
       }
    },
    state: {
        mainHeader: true
    },
    getters: {
        isMainHeaderActive(state){
            return state.mainHeader
        },
    },
}