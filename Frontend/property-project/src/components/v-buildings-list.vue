<template> 
    <div id="buildings-list-begin">  
        <!-- {{ searchId }}  -->

        <div class='flex'>
            <TransitionList of="buildings">
                <div key="buildings" v-if="count > 0" class="m-auto">
                    <TransitionList of="buildings">
                        <div :key="searchId" class="grid grid-cols-2 xl:grid-cols-3 items-center justify-center gap-2 md:gap-8 my-20">
                            <vBuildingCard  
                            v-for="building in buildings" 
                            :key="building.slug" 
                            :building="building" 
                            />    
                        </div>
                    </TransitionList>    
                </div>      
                <div key="no-results" v-else class="grid justify-center w-full"> 
                    <!-- <TransitionList> -->
                        <h2 :if="count == 0" class="text-2xl font-bold text-gray-600">По вашему запросу ничего не найдено :с</h2>
                <!-- </TransitionList> -->
                </div>
            </TransitionList>
        </div>
        <!-- <vPagination>

        </vPagination> -->
    </div>
</template>

<script>

import vBuildingCard from './v-building-card.vue';
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
        vBuildingCard,
        TransitionList,
        // vPagination,
    },
    computed: {
        ...mapGetters(['allBuildings','buildingsCount','currentBuildingPage','activeFindParams', 'searchId']),
        // animatedNumber: function() {
        //     return this.numberOfBuildings.toFixed(0);
        // },
        buildings(){
            if(this.certainBuildigns){
                return this.certainBuildigns
            }
            return this.allBuildings
        },
        count(){
            if(this.certainBuildigns){
                return this.certainBuildigns.length
            }
            return this.buildingsCount
        }
    },
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