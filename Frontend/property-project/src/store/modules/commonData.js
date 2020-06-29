
export default {
    mutations: {
       changeMainHeader(state, value){
           state.mainHeader = Boolean(value)
       },
       updateShowFlatsOnly(state, show){
        state.showFlatsOnly = Boolean(show)
    },
    //    changeLoadingState(state, value){
    //        state.loaded = Boolean(value)
    //    }
    },
    state: {
        mainHeader: false,
        showFlatsOnly: false,
        
        // loaded: true,
    },
    getters: {
        isMainHeaderActive(state){
            return state.mainHeader
        },
        showFlatsOnly(state){
            return state.showFlatsOnly
        },
        
        // isLoaded(state){
        //     return state.loaded
        // }
    },
}