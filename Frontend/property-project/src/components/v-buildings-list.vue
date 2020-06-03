<template> 
    <div>   
        <div class="text-center text-lg">Найдено: {{ buildingsCount }}</div>
        <div v-if="buildingsCount > 0" class="grid m-auto sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 justify-center gap-4 my-20">
            <vBuildingCard  
            v-for="building in allBuildings" 
            :key="building.slug" 
            :building="building" 

            />    
        </div>          
        <div v-else class="grid justify-center"> 
            <h2>По вашему запросу ничего не найдено :с</h2>
        </div>
    </div>
</template>

<script>

import vBuildingCard from './v-building-card.vue';
import {mapGetters} from 'vuex'
export default{
    data(){
        return {
            isMouseOver: false
        }
    },
    components: {
        vBuildingCard,
    },
    // computed: {
    //     allBuildings(){
    //         console.log(this.$store.getters.allBuildings)
    //         return this.$store.getters.allBuildings;
    //     }
    // },
    computed: {
        ...mapGetters(['allBuildings','buildingsCount'])
        },
    // methods: mapActions(['searchBuildings']),
    // async mounted() {
    //     this.searchBuildings();
    // },
}

</script>