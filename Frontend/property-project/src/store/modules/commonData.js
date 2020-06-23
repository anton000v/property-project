
export default {
    mutations: {
       changeMainHeader(state, value){
           state.mainHeader = Boolean(value)
       },
    //    changeLoadingState(state, value){
    //        state.loaded = Boolean(value)
    //    }
    },
    state: {
        mainHeader: false,

        // loaded: true,
    },
    getters: {
        isMainHeaderActive(state){
            return state.mainHeader
        },
        // isLoaded(state){
        //     return state.loaded
        // }
    },
}