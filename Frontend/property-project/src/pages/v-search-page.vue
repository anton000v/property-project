<template>  
    <div>
        <section class="pb-20 -mt-20">
            <div class="container mx-auto md:px-8" v-if="loaded">
                <!-- {{ this.activeFindParams }} -->
                <BuildingsSearchKit />
                <vBuildingsCounter v-if="!showFlatsOnly"/>
                <TransitionList>
                    <FlatsList v-if="showFlatsOnly"/>
                </TransitionList>
                <TransitionList>
                    <BuildingsList v-if="!showFlatsOnly"/>
                </TransitionList>
                
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
import TransitionList from '../transitions/list'
// import { addHashToLocation } from '../utils.js'
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
        TransitionList
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
        ]),
        async prepareData(){
            if(this.showFlatsOnly){
                await this.searchFlats(this.activeFindParams)
            }
            else{
                await this.searchBuildings(this.activeFindParams)
            }
        },
        setInitialData(){
            // if(this.$route.)
            // console.log('router:', this.$router)
            // console.log('route:', this.$route)
 
              this.updateFindParams(JSON.parse(JSON.stringify(this.$route.query)))
        },
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
            if(newVal){
                this.$router.push({name:'search-flats'})
                this.searchFlats()
            }
            else{
                this.$router.push({name:'search-page'})
                this.searchBuildings()
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