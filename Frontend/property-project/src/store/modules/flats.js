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
                const totalPages = resp.data.total_pages
                const currentPage = resp.data.current
                const nextPageLink = resp.data.next
                const previousPageLink = resp.data.previous
                // const perPage = resp.data.per_page
                console.log('FOUND Flats')
                console.log(foundFlats)
                ctx.commit('updateFlats', foundFlats)
                ctx.commit('updateFlatsCount', flatsCount)
                ctx.commit('updateFlatsTotalPages', totalPages)
                ctx.commit('updateFlatsCurrentPage', currentPage)
                ctx.commit('updateFlatsNextPageLink', nextPageLink)
                ctx.commit('updateFlatsPreviousPageLink', previousPageLink)
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

        updateFlats(state, buildings){
            state.buildings = buildings
        },
        updateFlatsCount(state, count){
            state.buildingsCount = count
        },
        updateFlatsTotalPages(state, totalPages){
            state.totalPages = totalPages
        },
        updateFlatsCurrentPage(state, currentPage){
            state.currentPage = currentPage
        },
        updateFlatsNextPageLink(state, nextPageLink){
            state.nextPageLink = nextPageLink
        },
        updateFlatsPreviousPageLink(state, previousPageLink){
            state.previousPageLink = previousPageLink
        },
        updateFlatsSearchId(state, searchId){
            state.searchId = searchId
        },
    },

    state: {

        flats: [],
        // buildingsOnMap: [],
        flatsSearchId: '',
        flatsBuildingsCount: 0,
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
            return state.flatsBuildingsCount
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