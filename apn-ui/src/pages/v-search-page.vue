<template>  
    <div>
        <section class="pb-20 -mt-20">
            <div class="container mx-auto md:px-8" v-if="loaded">
                <!-- {{ this.activeFindParams }} -->
                <BuildingsSearchKit />
                <vBuildingsCounter/>
                <!-- <TransitionList> -->
                    <FlatsList key="flats" v-if="showFlatsOnly"/>
                <!-- </TransitionList> -->
                <!-- <TransitionList> -->
                    <BuildingsList key="buildings" v-if="!showFlatsOnly"/>
                <!-- </TransitionList> -->
                
                <vPagination/>
            </div>
        </section>
    </div>
</template>

<script>

import BuildingsList from '../components/v-buildings-list'
import FlatsList from '../components/v-flats-list'
import BuildingsSearchKit from '../components/v-buildings-search-kit'
import { mapActions, mapGetters ,mapMutations } from 'vuex'
import vBuildingsCounter from '../components/v-buildings-counter'
import vPagination from '../components/v-pagination' 
// import TransitionList from '../transitions/list'
import { addHashToLocation } from '../utils.js'
export default {

    data(){
        return {
            loaded: false
        }
    },
    components: {
        BuildingsList,
        BuildingsSearchKit,
        vBuildingsCounter,
        vPagination,
        FlatsList,
        // TransitionList
    },
    methods: {
        ...mapActions([
            'searchBuildings', 
            'actionUpdateFindParams',
            'searchFlats'
        ]),
        ...mapMutations([
            'updateFindParams',
            'changeLoadingState',
            'updateShowFlatsOnly'
        ]),
        async prepareData(){
            if(this.showFlatsOnly){
                console.log('ACTIVE FIND PARAMS AAAAA: ', this.activeFindParams)
                await this.searchFlats(this.activeFindParams)
                this.callAddHashToLocation()
            }
            else{
                await this.searchBuildings(this.activeFindParams)
            }
        },
        setInitialData(){

                // if(this.$route.name=="search-buildings" || this.$route.name == 'home'){
                //     alert(1)
                // }
                this.updateFindParams(JSON.parse(JSON.stringify(this.$route.query)))
                if(this.$route.name=="search-flats"){
                    this.updateShowFlatsOnly(true)

                }
                // else{
                //     console.log('Router:', this.$route.name)
                // }

        },        
        callAddHashToLocation() {
          addHashToLocation(this.activeFindParams, this.$route.path)
        }
        // callAddHashToLocation() {
        //   addHashToLocation(this.activeFindParams, this.$route.path)
        // }
    },

    computed: {
      ...mapGetters([
        'activeFindParams', 
        'showFlatsOnly'
        ]),
    },

    created() {
      this.setInitialData()
    },
    watch:{        
        showFlatsOnly(newVal){
            // this.updateFindParams({})
            if(this.loaded){
                if(newVal){
                    this.$router.push({name:'search-flats'})
                    this.searchFlats()
                }
                else{
                    this.$router.push({name:'search-buildings'})
                    this.searchBuildings()
                }
            }

        }
    },
    mounted(){
      this.prepareData()
        .then(() => {
            this.loaded = true
            }
        )   
    },
    // before
}
</script>