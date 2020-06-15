
<template>
    <div v-if="loading">
    <!-- <section class="pb-20 -mt-32"> -->
        <vHeaderLittle/>
        <section class="pb-20 -mt-20">
            <div class="container mx-auto px-2 md:px-8">

                <div class="flex flex-wrap ">
                    
                        <!-- <div @click="$router.back(-1)" class=" invisible md:visible cursor-pointer w-auto left-0 bg-red-300">
                            <div class='ml-2 mr-2 text-2xl text-white text-center'>
                                Назад
                            </div>
                        
                        </div> -->
                    <div class="w-full text-center"> 
                        <!-- <div @click="$router.back(-1)" class=" invisible md:visible cursor-pointer w-auto left-0 bg-red-300">
                            <div class='ml-2 mr-2 text-2xl text-white text-center'>
                                Назад
                            </div>
                        </div> -->
                    
                        <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg">
                            <div class="px-4 py-5 flex-auto">
                                <div >
                                    ЖК ... 
                                </div>
                                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                                    <div class="cursor-pointer" @click="openMainImage">
                                        <img v-if="building.building_images[0]" :src="building.building_images[0].building_image" alt="">
                                    </div>
                                    <div class="col-span-2">
                                        инфо
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div
                            class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
                        >
                            <div class="px-4 py-5 flex-auto" v-if="building_images.length > 0 || layout_images.length >0">
                                <div>
                                    <div v-if="building_images.length > 0">
                                        <h2>Изображения дома</h2>
                                        <div>
                                            <building-gallary 
                                                ref="buildings" 
                                                gallaryRef="buildingsGallary" 
                                                :images_src="building_images" 
                                                caption="Изображение дома"
                                            >
                                            </building-gallary>
                                        </div>
                                    </div>
                                    <div v-if="layout_images.length > 0">
                                        <h2>Планировки</h2>
                                        <div>
                                            <building-gallary :images_src="layout_images" caption="Планировка"></building-gallary>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
    <!-- </section> -->
</template>

<script>
import BuildingGallary from '../components/v-building-gallary'
import { baseApiAddress } from '../variables'
import vHeaderLittle from '../components/v-header-little'
export default {
    // props:{
    //     slug:{
    //         type: String,
    //     }
    // },
    components:{
        BuildingGallary,
        vHeaderLittle
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
        },
        openMainImage(){
            console.log("Вот так вот:")
            console.log(this.$refs.buildings.$refs.buildingsGallary.$el)
            this.$refs.buildings.$refs.buildingsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
        }
    },
      computed: {
        building_images: function (){
            let images = []
            this.building.building_images.forEach(function(entry) {
                images.push(entry.building_image)
            });
            return images
        },
        layout_images: function () {
            let images = []
            this.building.layout_images.forEach(function(entry) {
                images.push(entry.layout_image)
            });
            return images
        }
    },
}
</script>

