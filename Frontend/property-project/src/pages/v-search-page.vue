<template>  
    <div>
        <Header/>
        <section class="pb-20 bg-gray-300 -mt-32">
            <div class="container mx-auto px-8">
                <BuildingsSearchKit/>
                <BuildingsList/>
            </div>
        </section>
    </div>
</template>

<script>

import Header from '../components/v-header'
import BuildingsList from '../components/v-buildings-list'
import BuildingsSearchKit from '../components/v-buildings-search-kit'
import { mapActions } from 'vuex'

export default {
    props:{
        findParams: {
            type: Object,
            default: function () { return {} }
        }
    },
    components: {
        BuildingsList,
        BuildingsSearchKit,
        Header
    },
    methods: {
        ...mapActions([
            'searchBuildings', 
        ]),
    },
    async mounted() {
    //   alert(this.findParams)
        // if(Object.keys(this.findParams).length > 0){
            
        // }
        // else{

        // }
        this.searchBuildings(this.findParams);
    },
    // computed: {
    //   ...mapGetters([
    //     'activeFindParams', 
    //     ])
    // },
}
</script>