<template> 
    <div id="flats-list-begin">  
        <!-- {{ searchId }}  -->
        <!-- {{ flatBuildingArr }} -->
        <div class='flex'>
            <TransitionList>
                <div key="buildings" v-if="count > 0" class="m-auto">
                    <TransitionList>
                        <div :key="searchId" class="grid grid-cols-2 xl:grid-cols-3 items-center justify-center gap-2 md:gap-8 my-20">
                            <vFlatCard  
                            v-for="flat in allFlats" 
                            :key="flat.id" 
                            :flat="flat" 
                            />    
                        </div>
                    </TransitionList>    
                </div>      
                <div key="no-results" v-else class="grid justify-center w-full"> 
                    <h2 :if="count == 0" class="text-2xl font-bold text-gray-600">По вашему запросу ничего не найдено :с</h2>
                </div>
            </TransitionList>
        </div>
        <!-- <vPagination>

        </vPagination> -->
    </div>
</template>

<script>

import vFlatCard from './v-flat-card';
import TransitionList from '../transitions/list'
import {mapGetters} from 'vuex'
// import {TweenLite} from 'gsap'
// import vPagination from './v-pagination' 

export default{
    props:{
        certainBuildigns: {
            type: Array,
            default: null
        }
    },
    data(){
        return {
            // numberOfBuildings: 0
        }
    },
    components: {
        vFlatCard,
        TransitionList,
        // vPagination,
    },
    computed: {
        ...mapGetters(['flatsCount', 'allFlats']),
        // animatedNumber: function() {
        //     return this.numberOfBuildings.toFixed(0);
        // },
        buildings(){
            if(this.certainBuildigns){
                return this.certainBuildigns
            }
            return this.allBuildings
        },
        // count(){
        //     if(this.certainBuildigns){
        //         return this.certainBuildigns.length
        //     }
        //     return this.buildingsCount
        // },
        // flatBuildingArr(){
        //     let flatBuildingArr = []


        //     this.allBuildings.forEach(building => {
        //         if(building.flats_for_sale.length > 0){
        //             building.flats_for_sale.forEach(flat => {
        //                 console.log(building)
        //                 console.log(flat)
        //                 flatBuildingArr.push({'building' : building,'flat' : flat})
        //                 // flatBuildingArr.push({'flat' : flat})
        //             })
        //         }
        //     });
        //     console.log('flatBuildingsPair:', flatBuildingArr)
        //     return flatBuildingArr
        // }
    },
    // methods:{
    //     ...mapMutations([
    //         'updateFlats'
    //     ])
    // },
    // mounted() {
        // this.updateFlats()
        // alert()
    // },
    // methods:{
    //     animateCounter(val){
    //         TweenLite.to(this.$data, { 
    //             duration: 0.5,
    //             numberOfBuildings: val,
    //             });
    //     }
    // },
    // watch: {
    //     buildingsCount: function(val) {
    //         this.animateCounter(val)
    //     }
    // },
    // mounted(){
    //     if(this.buildingsCount > 0){
    //         this.animateCounter(this.buildingsCount)
    //     }
    // },
    
}

</script>