<template>
    <div>
        <section class="pb-20 -mt-20">
            <div class="container mx-auto md:px-8">
                <vBackButton />
                <vMapSearchKit/>
                <vBuildingsCounter :countByBuildingsArr='true'/>
                <div class="h-full">
                    <div class="m-auto px-10 xl:px-5">
                        <div class="">
                            <vSearchableMap :buildings="buildingsForMap"/>
                             <!-- <vBuildingPreview v-for="building in allBuildings" :key="building.slug" :slug="building.slug" :building="building"/> -->
                        </div>
                    </div>
                    <div class="pt-12" v-if="buildingsForList.length > 0">
                        <p class="px-2 md:px-0">Так же есть вот такие новострои, которые еще строятся. Они не имеют адресса и не могут быть отображены на карте:</p>
                        <!-- <div class="grid grid-cols-4"> -->
                            <vBuildingsList :certainBuildigns="buildingsForList"/>
                        <!-- </div> -->
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import vMapSearchKit from '../components/v-map-search-kit'
import vBackButton from '../components/v-back-button'
import vSearchableMap from '../components/v-searchable-map'
import { mapActions, mapGetters ,mapMutations } from 'vuex'
// import vBuildingPreview from '../components/v-building-preview'
import vBuildingsCounter from '../components/v-buildings-counter'
import vBuildingsList from '../components/v-buildings-list'
export default {
    components:{
        vMapSearchKit,
        vBackButton,
        vSearchableMap,
        // vBuildingPreview,
        vBuildingsCounter,
        vBuildingsList
    },
    data(){
        return {
            loaded: false
        }
    },
    methods: {
        ...mapActions([
            'searchBuildings', 
            'actionUpdateFindParams',
            'mapSearchBuildings'
        ]),
        ...mapMutations([
            'updateFindParams',
            'changeLoadingState',
        ]),
        async prepareData(){
          await this.mapSearchBuildings(this.activeFindParams)
        },
        setInitialData(){
          this.updateFindParams(JSON.parse(JSON.stringify(this.$route.query)))
        },
        // show (slug) {
        // this.$modal.show('building-preview:'+slug);
        // },
        // hide (slug) {
        //     this.$modal.hide('building-preview:'+slug);
        // },
    },
    computed: {
      ...mapGetters([
        'activeFindParams', 
        'allBuildings'
        ]),
        buildingsForMap(){
            console.log()
            return this.allBuildings.filter(building => (building.lat != null && building.lng != null));
        },
        buildingsForList(){
            let buildings = this.allBuildings.filter(building => (building.lat == null || building.lng == null));
            // alert(buildings)
            // if(!Array.isArray(buildings)){
            //     buildings = [buildings]
            // }
            return buildings
        }
    },
    created() {
      this.setInitialData()
      
    },
    mounted(){
      // this.changeLoadingState(false)
    //   if(this.allBuildings.length == 0){
        this.prepareData()
                .then(() => {
                    this.loaded = true
                    }
                )   
    //     }
    //   else{
    //       this.loaded = true
    //   }
      // this.updateBuildings()   
    },
}
</script>