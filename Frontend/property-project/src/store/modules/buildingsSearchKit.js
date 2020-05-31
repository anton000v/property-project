// function arrCompareForSearch(a1,a2){
//     if(typeof a2 === 'undefined' || a2.length == 0){
//       return true
//     }
//     if(typeof a1 === 'undefined'){
//       return false
//     }
//     return a1.length == a2.length && a1.every((v,i)=>v === a2[i])
// }
// let session = context.rootState.instance.session;
import { saltovkaDBValue, severnayaSaltovkaDBValue } from '../../variables.js'
export default {
    actions: {
        // addStreet(ctx, selectedStreet){
        //     ctx.commit('addStreet', selectedStreet)
        // },

        checkToShowMicroDistricts(ctx, selectedValue){
            if(selectedValue == saltovkaDBValue){
              if(!ctx.getters.isSaltovkaDistrictChoosen){
                // alert('Салтовка выбрана!')
                // this.isSaltovkaDistrictChoosen = true
                ctx.commit('updateIsSaltovkaDistrictChoosen', true)
              }
            }
            else if(selectedValue == severnayaSaltovkaDBValue){
              if(!ctx.getters.isSevernayaSaltovkaDistrictChoosen){
                // alert('Северная салтовка выбрана!')
                // this.isSevernayaSaltovkaDistrictChoosen = true
                ctx.commit('updateIsSevernayaSaltovkaDistrictChoosen', true)
              }
            }
        },
        checkToHideMicroDistricts(ctx, removedValue){
            if(removedValue == saltovkaDBValue){
              if(ctx.getters.isSaltovkaDistrictChoosen){
                // alert('Салтовка выключена!')
                // this.isSaltovkaDistrictChoosen = false
                ctx.commit('updateIsSaltovkaDistrictChoosen', false)
              }
            }
            else if(removedValue == severnayaSaltovkaDBValue){
              if(ctx.getters.isSevernayaSaltovkaDistrictChoosen){
                // alert('Северная салтовка выключена!')
                // this.isSevernayaSaltovkaDistrictChoosen = false
                ctx.commit('updateIsSevernayaSaltovkaDistrictChoosen', false)
              }
            }
        }
    },
    mutations: {
        // addStreet(state, streets){
        //     // if(arrCompareForSearch(state.streets, streets)){
        //         // alert()
        //         state.streets.push(streets)
        //     // }
        // },
        // removeStreet(state, removedValue){
        //     const index = state.streets.indexOf(removedValue);
        //     if (index > -1) {
        //         state.streets.splice(index, 1);
        //     }
        // },
        // updateDistricts(state, districts){
        //     // if(arrCompareForSearch(state.districts, districts)){
        //         state.districts = districts
        //     // }
        // },
        // updateAdministrativeDistricts(state, administrativeDistricts){
        //     // if(arrCompareForSearch(state.administrativeDistricts, administrativeDistricts)){
        //         state.administrativeDistricts = administrativeDistricts
        //     // }
        // },
        // updateHouseNumbers(state, houseNumbers){
        //     // if(arrCompareForSearch(state.houseNumbers, houseNumbers)){
        //         state.houseNumbers = houseNumbers
        //     // }
        // },
        // updateSaltovkaMicroDistricts(state, saltovkaMicroDistricts){
        //     // if(arrCompareForSearch(state.saltovkaMicroDistricts, saltovkaMicroDistricts)){
        //         state.saltovkaMicroDistricts = saltovkaMicroDistricts
        //     // }
        // },
        // updateSevernayaSaltovkaMicroDistricts(state, severnayaSaltovkaMicroDistricts){
        //     // if(arrCompareForSearch(state.severnayaSaltovkaMicroDistricts, severnayaSaltovkaMicroDistricts)){
        //         state.severnayaSaltovkaMicroDistricts = severnayaSaltovkaMicroDistricts
        //     // }
        // },
        // updateDevelopers(state,developers){
        //     // if(arrCompareForSearch(state.developers, developers)){
        //         state.developers = developers
        //     // }
        // },
        addFindParam(state, dictVal){
            // alert(dictVal.value)
            if('key' in dictVal && 'value' in dictVal){
                if(dictVal.key in state.findParams){
                    state.findParams[dictVal.key].push(dictVal.value)
                }
                else{
                    state.findParams[dictVal.key] = [dictVal.value,]
                }  
                console.log('!! PARAMS')
                console.log(state.findParams)
            }
        },
        removeFindParam(state, dictVal){
            const index = state.findParams[dictVal.key].indexOf(dictVal.value);
            if (index > -1) {
                state.findParams[dictVal.key].splice(index, 1);
            }
        },
        updateIsSaltovkaDistrictChoosen(state, value){
            state.isSaltovkaDistrictChoosen = Boolean(value)
        },
        updateIsSevernayaSaltovkaDistrictChoosen(state, value){
            state.isSevernayaSaltovkaDistrictChoosen = Boolean(value)
        }
    },
    state: {
        streets:[],
        districts: [],
        administrativeDistricts:[],
        houseNumbers:[],
        saltovkaMicroDistricts:[],
        severnayaSaltovkaMicroDistricts:[],
        developers:[],
        findParams:{},
  
        isSaltovkaDistrictChoosen: false,
        isSevernayaSaltovkaDistrictChoosen: false,
  
    },
    getters: {
        selectedStreets(state){
            return state.streets
        },
        activeFindParams(state){
            return state.findParams
        },
        isSaltovkaDistrictChoosen(state){
            return state.isSaltovkaDistrictChoosen
        },
        isSevernayaSaltovkaDistrictChoosen(state){
            return state.isSevernayaSaltovkaDistrictChoosen
        }
    },
}