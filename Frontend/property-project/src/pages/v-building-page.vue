
<template>
    <div v-if="loading">
    <!-- <section class="pb-20 -mt-32"> -->
        <vHeaderLittle/>
        <section class="pb-20 -mt-20">
            <div class="container mx-auto  md:px-8">

                <div class="flex flex-wrap ">
                    
                        <!-- <div @click="$router.back(-1)" class=" invisible md:visible cursor-pointer w-auto left-0 bg-red-300">
                            <div class='ml-2 mr-2 text-2xl text-white text-center'>
                                Назад
                            </div>
                        
                        </div> -->
                    <div class="w-full"> 
                        <!-- <div @click="$router.back(-1)" class=" invisible md:visible cursor-pointer w-auto left-0 bg-red-300">
                            <div class='ml-2 mr-2 text-2xl text-white text-center'>
                                Назад
                            </div>
                        </div> -->
                    
                        <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg">
                            <div class="px-4 py-5 flex-auto">
                                <div class="text-2xl">
                                    <p class="uppercase font-bold  text-myMint-400">ЖК {{ building.name }}</p>
                                    <p>{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
                                </div>
                                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 pt-6">
                                    <div class="cursor-pointer" @click="openMainImage">
                                        <img v-if="building.building_images[0]" :src="building.building_images[0].building_image" alt="Главное фото">
                                        <img v-else-if="building.layout_images[0]" :src="building.layout_images[0].layout_image" alt="Главное фото">
                                        <img v-else :src="require('@/assets/images/cat-no-photo-yet-green-2.jpg')" alt="Главное фото">
                                    </div>
                                    <div class="col-span-1">
                                        <div class= 'h-full w-full'>

                                            <div class="grid grid-cols-2 justify-center text-center justify-center gap-2">
                                                <div class="flex-1 flex-col bg-gray-200 ">
                                                    <div class="text-gray-700 font-bold text-center bg-gray-400 px-4 py-2 m-2">
                                                        <div class="inline-flex items-center">
                                                            <HomeCityIcon fillColor="#1F7B67" :size="25" />
                                                            <div class="flex-1 px-2 text-sm lg:text-base">
                                                                Административный район
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="flex-1 text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.administrative_district }}</div>
                                                </div>
                                                <div class="flex-1 flex-col bg-gray-200 ">
                                                    <div class="text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-2">
                                                        <div class="inline-flex items-center">
                                                            <HomeGroupIcon fillColor="#1F7B67" :size="25" />
                                                            <div class="flex-1 px-2">
                                                                Район
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="flex-1 text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.district }}</div>
                                                </div>
                                                <div v-if="building.micro_district !== 'Не делится на микрорайоны'" class="flex-1 flex-col bg-gray-200 ">
                                                    <div class="text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-2">
                                                        <div class="inline-flex items-center">
                                                            <DomainIcon fillColor="#1F7B67" :size="25" />
                                                            <div class="flex-1 px-2">
                                                                Микрорайон
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="flex-1 text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.micro_district }}</div>
                                                </div>
                                                <div class="flex-1 flex-col bg-gray-200 ">
                                                    <div class="text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-2">
                                                        <div class="inline-flex items-center">
                                                            <HouseEditIcon fillColor="#1F7B67" :size="25" />
                                                            <div class="flex-1 px-2">
                                                                Застройщик
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.developer }}</div>
                                                </div>
                                            </div>
                                            <div class="flex1 bg-gray-200 mt-5" v-if="building.ways_from_metro.length">
                                                <div class="px-2 py-2">
                                                    <div class="text-gray-700 font-bold  text-center bg-gray-400">
                                                        <div class="inline-flex items-center">
                                                            <highway-icon fillColor="#1F7B67" :size="30" />
                                                            <div class="flex-1 my-2 px-4 py-2">
                                                                Пути от метро
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="flex-1 text-gray-700 text-center bg-gray-400 ">
                                                        <div class="w-full flex text-sm lg:text-base justify-center lg:my-2 lg:px-4 lg:py-2" v-for="way in building.ways_from_metro" :key="way.metro">
                                                            <div class="w-2/5"> {{ way.metro }} </div>
                                                            <div class="w-1/5"> {{ way.type_of_movement }} </div>
                                                            <div class="w-1/5"> {{ way.time }} мин. </div>
                                                            <div class="w-1/5"> {{ way.number_of_meters }} м. </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="flex1 bg-gray-200 mt-5" v-if="building.ways_from_metro.length">
                                               <div class="text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-2">
                                                            <div class="inline-flex items-center">
                                                                <ClipboardCheckMultipleIcon fillColor="#1F7B67" :size="25" />
                                                                <div class="flex-1 px-2">
                                                                    Сдан в эксплуатацию
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.completion_date }}</div>
                                            </div>
                                         </div>
                                    </div>
                                </div>
                            </div>
                        </div>


<div ref="anchors-default-position" class="invisible"> </div>
<div ref="anchors" class="sticky text-center  left-0 top-0 z-50 bg-myPageBackground relative flex flex-col min-w-0 shadow-md ">
    <transition name="fade">
            <div v-if="anchorsInfo.showAncorsTitle" class='flex-1'>
                <p class='text-center text-myMint-400 text-base text-gray-700'>Property-project Харьков | {{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
            </div>
            <!-- <div v-else class='h-4'>
            </div> -->
    </transition>
    <scrollactive  active-class="bg-myMint-100" :modifyUrl="false">
        <!-- <a href="#images" class="">Фото</a>
        <a href="#layouts" class="">Планировки</a> -->

         <ul class="flex">
            <li class="flex-1">
                <a href="#images" class="scrollactive-item transition duration-500 transform hover:translate-y-1 ease-in-out text-center block hover:bg-myMint-100 font-bold text-gray-700 hover:text-white  hover:shadow-xl py-2 ">
                    Изображения дома
                </a>
            </li>
            <li class="flex-1">
                <a href="#layouts" class="scrollactive-item transition duration-500 transform hover:translate-y-1 ease-in-out text-center block hover:bg-myMint-100 font-bold text-gray-700 hover:text-white hover:shadow-xl py-2 ">
                    Планировки
                </a>
            </li>
        </ul>
    </scrollactive>
</div>
  <!-- <div class="flex h-16 bg-myMint-400 text-white hover:bg-myMint-100 hover:text-black transition duration-500 ease-in-out hover:rounded-none hover:opacity-40 transform hover:translate-y-1 hover:shadow-2xl overflow-hidden shadow-md">  
                        <p class="m-auto text-xl"> Открыть полностью </p>
                    </div> -->
    

                    
                        <!-- <div
                            class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
                        > -->
                        <div
                            class="relative flex flex-col min-w-0 w-full pt-8 mb-8 rounded-lg"
                        >
                            <div class="flex-auto" v-if="building_images.length > 0 || layout_images.length > 0">
                                <div>
                                    <div id="images" class="py-5" v-if="building_images.length > 0">
                                        <h2 class="text-3xl font-bold pt-10 lg:pt-0 text-gray-700 text-center">Изображения дома</h2>
                                        <!-- <div class="flex w-full"> -->
                                        <div class="m-auto w-1/2 pt-3 mb-3 border-b-2 border-myMint-100 opacity-25"></div>
                                        <!-- </div> -->
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
                                    <div id="layouts" class="py-6" v-if="layout_images.length > 0">
                                        <h2 class="text-3xl font-bold pt-10 lg:pt-0 text-gray-700 text-center">Планировки</h2>
                                        <!-- <div class="flex w-full"> -->
                                            <div class="m-auto w-1/2 pt-3 mb-3 border-b-2 border-myMint-100 opacity-25"></div>
                                        <!-- </div> -->
                                        <div>
                                            <building-gallary :images_src="layout_images" caption="Планировка"></building-gallary>
                                        </div>
                                    </div>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                    <p>asdfdsf</p>
                                </div>
                            </div>
                            <div v-else>
                                <building-gallary 
                                    ref="buildings" 
                                    gallaryRef="buildingsGallary" 
                                    :images_src="[require('@/assets/images/cat-no-photo-yet-green-2.jpg')]" 
                                    caption="Кошечка лучше, чем ничего"
                                >
                                </building-gallary>
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
import HighwayIcon from 'vue-material-design-icons/Highway.vue';
import HouseEditIcon from 'vue-material-design-icons/HomeEdit';
import HomeCityIcon from 'vue-material-design-icons/HomeCity';
import HomeGroupIcon from 'vue-material-design-icons/HomeGroup';
import DomainIcon from 'vue-material-design-icons/Domain';
import ClipboardCheckMultipleIcon from 'vue-material-design-icons/ClipboardCheckMultiple';
// import debounce from 'lodash/debounce';
// import VueScrollactive from 'vue-scrollactive';


export default {
    // props:{
    //     slug:{
    //         type: String,
    //     }
    // },
    components:{
        BuildingGallary,
        vHeaderLittle,
        HighwayIcon,
        HouseEditIcon,
        HomeCityIcon,
        HomeGroupIcon,
        DomainIcon,
        ClipboardCheckMultipleIcon,
        
        // VueScrollactive
    },
    data(){
        return{
            building: {},
            loading: false,
            anchorsInfo: {showAncorsTitle: false},
            
        }
        
    },
    mounted() {
        if(this.$route.params.slug === undefined){
            this.$router.replace({name: 'page-404' })
        }
        this.prepareData()
            .then(() => {
                this.loading = true
                this.$nextTick(()=>{
                    this.updateAnchorsOffset()  
                });
                }
            )   
    },
    // ------ For animation eg
    created () {
         window.addEventListener('scroll', this.handleScroll);
         window.addEventListener('resize', this.updateAnchorsOffset);
            // this.anchorsOffsetTop = this.$refs.anchors.$el.offsetTop;
            // alert(this.anchorsOffsetTop)

    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll);
        window.removeEventListener('resize', this.updateAnchorsOffset);
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
        },
        // ---- for animation eg
        handleScroll () {
            // console.log('SCROLE'+event)
            if (window.pageYOffset > this.anchorsInfo.defaultPosition) {
                this.anchorsInfo.showAncorsTitle = true
                // this.anchorsInfo.element.classList.add("text-center");

            } else {
                this.anchorsInfo.showAncorsTitle = false
                // this.anchorsInfo.element.classList.remove("text-center");
            }
        },
        updateAnchorsOffset(){
            this.anchorsInfo.element = this.$refs.anchors;
            // this.anchorsInfo.anchorsOffset = this.anchorsInfo.element.offsetTop
            // console.log("Anchors offset: "+this.anchorsInfo.anchorsOffset)
            this.anchorsInfo.defaultPosition = this.$refs["anchors-default-position"].offsetTop 
            this.handleScroll()
            // console.log("Default anchor position"+this.anchorsInfo.defaultPosition)
        },
        // updateGallaryClass(){
        //     let gallaries = document.querySelectorAll('my-gallery');
        //     gallaries.forEach(
        // }
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

<style scoped>
.fade-enter-active{
  transition: opacity .5s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}


</style>
