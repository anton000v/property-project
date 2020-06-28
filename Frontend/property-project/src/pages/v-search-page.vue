<template>  
    <div>
        <section class="pb-20 -mt-20">
            <div class="container mx-auto md:px-8" v-if="loaded">
                <!-- {{ this.activeFindParams }} -->
                <BuildingsSearchKit />
                <vBuildingsCounter/>
                <BuildingsList/>
                <vPagination/>
            </div>
        </section>
    </div>
</template>

<script>

import BuildingsList from '../components/v-buildings-list'
import BuildingsSearchKit from '../components/v-buildings-search-kit'
import { mapActions, mapGetters ,mapMutations } from 'vuex'
import vBuildingsCounter from '../components/v-buildings-counter'
import vPagination from '../components/v-pagination' 
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
    },
    methods: {
        ...mapActions([
            'searchBuildings', 
            'actionUpdateFindParams',
            
        ]),
        ...mapMutations([
            'updateFindParams',
            'changeLoadingState',
        ]),
        async prepareData(){
          await this.searchBuildings(this.activeFindParams)
        },
        setInitialData(){
          this.updateFindParams(JSON.parse(JSON.stringify(this.$route.query)))
        },
    },

    computed: {
      ...mapGetters([
        'activeFindParams', 
        ]),
    },

    created() {
      this.setInitialData()
      
    },
    mounted(){
      // this.changeLoadingState(false)
      this.prepareData()
            .then(() => {
                this.loaded = true
                }
            )   
      // this.updateBuildings()   
    },
    // before
}
</script>