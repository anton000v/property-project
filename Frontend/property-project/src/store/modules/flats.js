export default {
    actions: {

        async searchFlats(ctx, findParams={}){
            const qs = require('qs');
            const axios = require('axios');
            const searchId = qs.stringify(findParams, {arrayFormat: 'repeat'})
            axios.get('http://127.0.0.1:8000/api/flats?'+ searchId, 
            // {
            //  searchId,
            // paramsSerializer: params => {
            //     // console.log('Find params while searching: ')
            //     // console.log(qs.stringify(params, {arrayFormat: 'repeat'}))  
            //     return qs.stringify(params, {arrayFormat: 'repeat'})
            // }
            // }
            ).then(resp => {
                const foundFlats = resp.data.results
                const flatsCount = resp.data.count
                const flatsTotalPages = resp.data.total_pages
                const flatsCurrentPage = resp.data.current
                const flatsNextPageLink = resp.data.next
                const flatsPreviousPageLink = resp.data.previous
                // const perPage = resp.data.per_page
                console.log('FOUND Flats')
                console.log(foundFlats)
                ctx.commit('updateFlats', foundFlats)
                ctx.commit('updateFlatsCount', flatsCount)
                ctx.commit('updateFlatsTotalPages', flatsTotalPages)
                ctx.commit('updateFlatsCurrentPage', flatsCurrentPage)
                ctx.commit('updateFlatsNextPageLink', flatsNextPageLink)
                ctx.commit('updateFlatsPreviousPageLink', flatsPreviousPageLink)
                ctx.commit('updateFlatsSearchId', searchId)
                // ctx.commit('updatePerPage', perPage)
            })
        }

        // checkToShowMicroDistricts(ctx, selectedValue){
        //     if(selectedValue == saltovkaDBValue){
        //       if(!ctx.getters.isSaltovkaDistrictChoosen){
        //         // alert('Салтовка выбрана!')
        //         // this.isSaltovkaDistrictChoosen = true
        //         ctx.commit('updateIsSaltovkaDistrictChoosen', true)
        //       }
        //     }
        //     else if(selectedValue == severnayaSaltovkaDBValue){
        //       if(!ctx.getters.isSevernayaSaltovkaDistrictChoosen){
        //         // alert('Северная салтовка выбрана!')
        //         // this.isSevernayaSaltovkaDistrictChoosen = true
        //         ctx.commit('updateIsSevernayaSaltovkaDistrictChoosen', true)
        //       }
        //     }
        // },
        // checkToHideMicroDistricts(ctx, removedValue){
        //     if(removedValue == saltovkaDBValue){
        //       if(ctx.getters.isSaltovkaDistrictChoosen){
        //         // alert('Салтовка выключена!')
        //         // this.isSaltovkaDistrictChoosen = false
        //         ctx.commit('updateIsSaltovkaDistrictChoosen', false)
        //       }
        //     }
        //     else if(removedValue == severnayaSaltovkaDBValue){
        //       if(ctx.getters.isSevernayaSaltovkaDistrictChoosen){
        //         // alert('Северная салтовка выключена!')
        //         // this.isSevernayaSaltovkaDistrictChoosen = false
        //         ctx.commit('updateIsSevernayaSaltovkaDistrictChoosen', false)
        //       }
        //     }
        // },
        // setDefaultDistrictsChoosen(ctx){
        //     ctx.commit('updateIsSaltovkaDistrictChoosen', false)
        //     ctx.commit('updateIsSevernayaSaltovkaDistrictChoosen', false)
        // }

    },
    mutations: {

        updateFlats(state, flats){
            state.flats = flats
        },
        updateFlatsCount(state, count){
            state.flatsCount = count
        },
        updateFlatsTotalPages(state, flatsTotalPages){
            state.flatsTotalPages = flatsTotalPages
        },
        updateFlatsCurrentPage(state, flatsCurrentPage){
            state.flatsCurrentPage = flatsCurrentPage
        },
        updateFlatsNextPageLink(state, nextPageLink){
            state.nextPageLink = nextPageLink
        },
        updateFlatsPreviousPageLink(state, previousPageLink){
            state.previousPageLink = previousPageLink
        },
        updateFlatsSearchId(state, searchId){
            state.flatsSearchId = searchId
        },
    },

    state: {

        flats: [],
        // buildingsOnMap: [],
        flatsSearchId: '',
        flatsCount: 0,
        flatsTotalPages: 0,
        flatsCurrentPage: 0,
        flatsNextPageLink: null,
        flatsPreviousPageLink: null,
  
    },
    getters: {

        allFlats(state){
            return state.flats
        },
        flatsCount(state){
            return state.flatsCount
        },
        flatsTotalPages(state){
            return state.flatsTotalPages
        },
        flatsCurrentPage(state){
            return state.flatsCurrentPage
        },
        flatsNextPageLink(state){
            return state.flatsNextPageLink
        },
        flatsPreviousPageLink(state){
            return state.flatsPreviousPageLink
        },
        flatsSearchId(state){
            return state.flatsSearchId
        },

    },
}