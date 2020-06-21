<template> 
    <div id="buildings-list-begin">  
        <!-- {{ searchId }}  -->
        <div class="text-center text-lg text-myMint-300 hover:text-myMint-100 font-bold transition duration-500">
            <div class="text-gray-500">Найдено:</div> 
            <div ref="buildingsCounter" class="text-4xl">{{ animatedNumber }}</div>
        </div>
        
        <TransitionList>
            <div key="buildings" v-if="buildingsCount > 0">
                <TransitionList>
                    <div :key="searchId" class="grid m-auto sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 justify-center gap-8 my-20">
                        <vBuildingCard  
                        v-for="building in allBuildings" 
                        :key="building.slug" 
                        :building="building" 
                        />    
                    </div>
                </TransitionList>    
            </div>      
            <div key="no-results" v-else class="grid justify-center"> 
                <!-- <TransitionList> -->
                    <h2 :if="buildingsCount == 0" class="text-2xl font-bold text-gray-600">По вашему запросу ничего не найдено :с</h2>
            <!-- </TransitionList> -->
            </div>
        </TransitionList>
        <vPagination>

        </vPagination>
    </div>
</template>

<script>

import vBuildingCard from './v-building-card.vue';
import TransitionList from '../transitions/list'
import {mapGetters} from 'vuex'
import {TweenLite} from 'gsap'
import vPagination from './v-pagination' 

export default{
    data(){
        return {
            numberOfBuildings: 0
        }
    },
    components: {
        vBuildingCard,
        TransitionList,
        vPagination
    },
    computed: {
        ...mapGetters(['allBuildings','buildingsCount','currentPage','activeFindParams', 'searchId']),
        animatedNumber: function() {
            return this.numberOfBuildings.toFixed(0);
        }
    },
    methods:{
        animateCounter(val){
            TweenLite.to(this.$data, { 
                duration: 0.5,
                numberOfBuildings: val,
                });
        }
    },
    watch: {
        buildingsCount: function(val) {
            this.animateCounter(val)
        }
    },
    mounted(){
        if(this.buildingsCount > 0){
            this.animateCounter(this.buildingsCount)
        }
    }
}

</script>