<template> 
    <div>      
        <div v-if="buildingsCount > 0" class="grid m-auto sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 justify-center gap-4 my-20">
            <PropertyCard v-for="building in allBuildings" :key="building.slug" :building="building"/>    
        </div>          
        <div v-else class="grid justify-center"> 
            <h2>По вашему запросу ничего не найдено :с</h2>
        </div>
    </div>
</template>

<script>

import PropertyCard from './PropertyCard.vue';
import {mapGetters} from 'vuex'
export default{
    components: {
        PropertyCard,
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