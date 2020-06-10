<template>
    <!-- <section class="pb-20 -mt-32"> -->
            <div class="container mx-auto px-8">
                <div v-if="loading">
                    <!-- {{building}} -->
                    <!-- {{ $route.params.slug }} -->
                    <!-- <div v-if="building.building_images.length > 0"> -->
                        <!-- {{ building_images }} -->
                        <h2>Изображения дома</h2>
                        <div>
                            <building-gallary :images_src="building_images" caption="Изображение дома"></building-gallary>
                        </div>

                        <h2>Планировки</h2>
                        <div>
                            <building-gallary :images_src="building_images" caption="Планировка"></building-gallary>
                        </div>
                    <!-- </div> -->
                </div>
            </div>
    <!-- </section> -->
</template>

<script>
import BuildingGallary from '../components/v-building-gallary'
import { baseApiAddress } from '../variables'
export default {
    // props:{
    //     slug:{
    //         type: String,
    //     }
    // },
    components:{
        BuildingGallary
    },
    data(){
        return{
            building: {},
            loading: false
        }
        
    },
    mounted() {
        if(this.$route.params.slug === undefined){
            this.$router.replace({name: 'page-404' })
        }
        this.prepareData()
            .then(() => this.loading = true)
    },
    methods: {
        async prepareData(){
            await this.searchBuildings()
        },

        async searchBuildings(){
            // const qs = require('qs');
            const axios = require('axios');
            await axios.get(baseApiAddress+'buildings/'+this.$route.params.slug, {
            // params: {
            //     slug:this.$route.params.slug
            //     }
            }).then(resp => {
            this.building = resp.data
            
            // const foundBuildings = resp.data.results
            // const buildingsCount = resp.data.count
            // console.log('FOUND BUILDINGS')
            // console.log(foundBuildings)
            // ctx.commit('updateBuildings', foundBuildings)
            // ctx.commit('updateBuildingsCount', buildingsCount)
            })
            console.log(this.building)
        }
    },
      computed: {
        building_images: function (){
                let images = []
                this.building.building_images.forEach(function(entry) {
                images.push(entry.building_image)
                });
            //     this.building.layout_images.forEach(function(entry) {
            //         images.push(entry.layout_image)
            // });
            return images
        }
    },
}
</script>

