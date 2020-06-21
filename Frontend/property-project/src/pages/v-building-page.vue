
<template>
    <div v-if="loading">
    <!-- <section class="pb-20 -mt-32"> -->
        <!-- <vHeaderLittle/> -->
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
                        <div class="relative rounded-lg flex md:hover:shadow-lg hover:bg-myMint-100 hover:text-white md:hover:text-gray-700 text-myMint-400 cursor-pointer" @click="$router.go(-1)">
                            <div class="w-full inline-flex items-center md:transition md:duration-500 md:ease-in-out  md:transform md:hover:-translate-x-10">
                                <!-- <div class=""> -->
                                    <KeyboardBackspaceIcon  :size="35"/>
                                <!-- </div> -->
                                <span class="pl-5">Назад</span>
                            </div>
                        </div>
                        <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg">
                            <div class="px-1 md:px-4 py-5 flex-auto">
                                <div class="text-2xl">
                                    <p class="uppercase font-bold text-gray-700">ЖК {{ building.name }}</p>
                                    <p class="text-gray-700 font-bold">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
                                </div>
                                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-6 pt-6">
                                    <div class="cursor-pointer" @click="openMainImage">
                                        <img v-if="building.building_images[0]" :src="building.building_images[0].building_image" alt="Главное фото">
                                        <img v-else-if="building.layout_images[0]" :src="building.layout_images[0].layout_image" alt="Главное фото">
                                        <img v-else :src="require('@/assets/images/cat-no-photo-yet-green-2.jpg')" alt="Главное фото">
                                    </div>
                                    <div class="col-span-1">
                                        <div class= 'h-full w-full'>

                                            <div class="grid grid-cols-2 justify-center text-center justify-center gap-2">
                                                <div v-if="building.administrative_district != null" class="flex-1 rounded-lg flex-col bg-gray-200 md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 font-bold text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <HomeCityIcon fillColor="#1F7B67" :size="25" />
                                                            <div class="block md:hidden flex-1 px-1 text-sm">
                                                                Админ. район
                                                            </div>
                                                            <div class="hidden md:block flex-1 px-2 text-sm lg:text-base">
                                                                Административный район
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="rounded-lg bg-white border-b border-myMint-100 text-myMint-400 font-bold text-center md:px-4 py-2 m-2">{{ building.administrative_district }}</div>
                                                </div>
                                                <div v-if="building.district != null" class="flex-1 rounded-lg flex-col bg-gray-200 md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 font-bold  text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <HomeGroupIcon fillColor="#1F7B67" :size="25" />
                                                            <div class="flex-1 sm:px-1 px-2 text-sm lg:text-base">
                                                                Район
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="rounded-lg bg-white border-b border-myMint-100 text-myMint-400 font-bold text-center md:px-4 py-2 m-2">{{ building.district }}</div>
                                                </div>
                                                <div v-if="building.micro_district !== 'Не делится на микрорайоны'" class="flex-1 rounded-lg flex-col bg-gray-200 md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <DomainIcon fillColor="#1F7B67" :size="25" />
                                                            <div class="flex-1 sm:px-1 px-2 text-sm lg:text-base">
                                                                Микрорайон
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="bg-white rounded-lg border-b border-myMint-100 text-myMint-400 font-bold  text-center md:px-4 py-2 m-1 md:m-2">{{ building.micro_district }}</div>
                                                </div>
                                                <div v-if="building.developer != null" class="flex-1 rounded-lg flex-col bg-gray-200 md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 font-bold  text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <HouseEditIcon fillColor="#1F7B67" :size="25" />
                                                            <div class="flex-1 sm:px-1 px-2 text-sm lg:text-base">
                                                                Застройщик
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="bg-white rounded-lg border-b border-myMint-100 border-myMint-100 text-myMint-400 font-bold  text-center  md:px-4 py-2 m-2">{{ building.developer }}</div>
                                                </div>
                                            </div>
                                            <div v-if="building.ways_from_metro != null && building.ways_from_metro.length > 0" class="flex1 rounded-lg bg-gray-200 mt-5 md:transition md:duration-500 md:hover:shadow-md" >
                                                <div class="px-2 py-2">
                                                    <div class="text-gray-700 font-bold  text-center">
                                                        <div class="inline-flex items-center">
                                                            <highway-icon fillColor="#1F7B67" :size="30" />
                                                            <div class="flex-1 m-1 md:m-2 px-4 p-2 text-sm lg:text-base">
                                                                Пути от метро
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="flex-1 text-center">
                                                        <div class="w-full rounded-lg bg-white border-b border-myMint-100 text-myMint-400 font-bold flex text-sm lg:text-base justify-center mt-2 lg:px-4 pb-2 pt-2" v-for="way in building.ways_from_metro" :key="way.metro">
                                                            <div class="w-2/5"> {{ way.metro }} </div>
                                                            <div class="w-1/5"> {{ way.type_of_movement }} </div>
                                                            <div class="w-1/5"> {{ way.time }} мин. </div>
                                                            <div class="w-1/5"> {{ way.number_of_meters }} м. </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div v-if="building.completion_date != null" class="flex1 rounded-lg bg-gray-200 mt-5 md:transition md:duration-500 md:hover:shadow-md" >
                                               <div class="text-gray-700 font-bold  text-center px-4 py-2 m-2">
                                                <div class="inline-flex items-center">
                                                    <ClipboardCheckMultipleIcon fillColor="#1F7B67" :size="25" />
                                                    <div class="flex-1 px-2 text-sm lg:text-base">
                                                        Сдан в эксплуатацию
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="rounded-lg bg-white border-b border-myMint-100 text-myMint-400 font-bold text-center md:px-4 py-2 m-2">{{ building.completion_date }}</div>
                                            </div>
                                         </div>
                                    </div>
                                </div>
                            </div>
                        </div>

<!-- <div class='p-10'> -->
    <div ref="anchors-default-position" class="invisible"> </div>
    <div ref="anchors" class="sticky text-center left-0 top-0 z-50 bg-myPageBackground relative flex flex-col min-w-0 shadow-md rounded-lg ">
        <div class="hidden md:block">
            <transition name="fade">
                    <div v-if="anchorsInfo.showAncorsTitle" class='flex-1 '>
                        <p class='text-center text-myMint-400 text-base text-gray-700'>Property-project Харьков | {{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
                    </div>
                    <!-- <div v-else class='h-4'>
                    </div> -->
            </transition>
        </div>
        <scrollactive  :offset="80" active-class="bg-myMint-100" :modifyUrl="false">
            <!-- <a href="#images" class="">Фото</a>
            <a href="#layouts" class="">Планировки</a> -->

            <ul class="flex text-sm md:text-base">
                <li class="flex-1">
                    <a href="#building-full-info" class="rounded-lg scrollactive-item md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-300 font-bold text-gray-700 md:hover:text-white md:hover:shadow-xl py-2 ">
                        Об обьекте
                    </a>
                </li>
                <li class="flex-1">
                    <a href="#images" class="rounded-lg  scrollactive-item md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-300 font-bold text-gray-700 md:hover:text-white  md:hover:shadow-xl py-2 ">
                        Изображения
                    </a>
                </li>
                <li class="flex-1">
                    <a href="#layouts" class="rounded-lg  scrollactive-item md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-300 font-bold text-gray-700 md:hover:text-white md:hover:shadow-xl py-2 ">
                        Планировки
                    </a>
                </li>
                <li class="flex-1">
                    <a href="#buildings-for-sale" class="rounded-lg  scrollactive-item md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-300 font-bold text-gray-700 md:hover:text-white md:hover:shadow-xl py-2 ">
                        В продаже
                    </a>
                </li>
            </ul>
        </scrollactive>
    </div>
<!-- </div> -->
  <!-- <div class="flex h-16 bg-myMint-400 text-white hover:bg-myMint-100 hover:text-black transition duration-500 ease-in-out hover:rounded-none hover:opacity-40 transform hover:translate-y-1 hover:shadow-2xl overflow-hidden shadow-md">  
                        <p class="m-auto text-xl"> Открыть полностью </p>
                    </div> -->
    

                    
                        <!-- <div
                            class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
                        > -->
                        <div
                            class="relative flex flex-col min-w-0 w-full pt-8 mb-8 rounded-lg"
                        >
                            <div class="flex-auto">
                                <div>
                                    <div id="building-full-info" class="mt-20 md:rounded-lg md:transition md:duration-500 md:transform " >
                                        <div class="mx-5">
                                            <h2 class="text-xl font-bold pt-10 lg:pt-0 text-gray-700 text-center">Характеристики ЖК</h2>
                                            <!-- <div class="flex w-full"> -->
                                            <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myMint-100 opacity-25"></div>
                                            <!-- </div> -->
                                            <div class='grid py-2 grid-cols-2'>
                                                <div v-if="building.the_class">Класс:<span class="px-4 font-bold text-myMint-400">{{ building.the_class }}</span></div>
                                                <div v-if="building.construction_technology">Технология строительства:<span class="px-4 font-bold text-myMint-400">{{ building.construction_technology }}</span></div>
                                                <div v-if="building.number_of_storeys">Этажность:<span class="px-4 font-bold text-myMint-400">{{ building.number_of_storeys }}</span></div>
                                                <div v-if="building.walls_type">Стены:<span class="px-4 font-bold text-myMint-400">{{ building.walls_type }}</span></div>
                                                <div v-if="building.number_of_buildings">Кол-во домов:<span class="px-4 font-bold text-myMint-400">{{ building.number_of_buildings }}</span></div>
                                                <div v-if="building.warming">Утепление:<span class="px-4 font-bold text-myMint-400">{{ building.warming }}</span></div>
                                                <div v-if="building.number_of_sections_or_entrances">Кол-во секций / подьездов:<span class="px-4 font-bold text-myMint-400">{{ building.number_of_sections_or_entrances }}</span></div>
                                                <div v-if="building.room_height">Высота помещений:<span class="px-4 font-bold text-myMint-400">{{ building.room_height }}</span></div>
                                                <div v-if="building.the_class" class="mt-5 col-span-2">Кол-во квартир в доме:<span class="px-4 font-bold text-myMint-400">{{ building.room_height }}</span></div>
                                                <div v-if="building.the_class" class="col-span-2">Кол-во квартир на этаж:<span class="px-4 font-bold text-myMint-400">{{ building.room_height }}</span></div>
                                                <div v-if="building.the_class" class="mt-5 col-span-2">Типы квартир:</div>
                                                <div v-if="building.the_class" class="mt-5 col-span-2">Коммерческие помещения:</div>

                                                <div class="">Коммуникации:</div>
                                                <div class="">Лифт:</div>
                                            </div>
                                        </div>
                                    </div>
                                    <div id="images" class="mt-20 md:rounded-lg md:transition md:duration-500 md:transform " >
                                        <h2 class="text-xl font-bold mt-10 lg:pt-0 text-gray-700 text-center">Изображения дома</h2>
                                        <!-- <div class="flex w-full"> -->
                                        <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myMint-100 opacity-25"></div>
                                        <!-- </div> -->
                                        <div>
                                            <building-gallary 
                                                v-if="building.building_images.length > 0"
                                                ref="buildings" 
                                                gallaryRef="buildingsGallary" 
                                                :images_src="building_images" 
                                                caption="Изображение дома"
                                            >
                                            </building-gallary>

                                            <building-gallary 
                                                v-else
                                                ref="buildings" 
                                                gallaryRef="buildingsGallary" 
                                                :images_src="[require('@/assets/images/cat-no-photo-yet-green-2.jpg')]" 
                                                caption="Кошечка лучше, чем ничего"
                                            >
                                            </building-gallary>
                                        </div>
                                    </div>
                                    <div id="layouts" class="mt-20 md:rounded-lg md:transition md:duration-500 md:transform ">
                                        <h2 class="text-xl font-bold mt-10 lg:pt-0 text-gray-700 text-center">Планировки</h2>
                                        <!-- <div class="flex w-full"> -->
                                            <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myMint-100 opacity-25"></div>
                                        <!-- </div> -->
                                        <div>
                                            <building-gallary 
                                            v-if="building.layout_images.length > 0"
                                            ref="layouts"
                                            gallaryRef="layoutsGallary" 
                                            :images_src="layout_images" 
                                            caption="Планировка">
                                            </building-gallary>

                                            <building-gallary 
                                                v-else
                                                ref="layouts" 
                                                gallaryRef="layoutsGallary" 
                                                :images_src="[require('@/assets/images/cat-no-photo-yet-green-2.jpg')]" 
                                                caption="Кошечка лучше, чем ничего"
                                            >
                                            </building-gallary>
                                        </div>
                                    </div>
                                    <div id="buildings-for-sale" class="mt-20 md:rounded-lg md:transition md:duration-500 md:transform " >
                                        <h2 class="text-xl font-bold mt-10 lg:pt-0 text-gray-700 text-center">Обьекты в продаже</h2>
                                        <!-- <div class="flex w-full"> -->
                                        <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myMint-100 opacity-25"></div>
                                        <!-- </div> -->
                                        <div>
        
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- <div v-else>
                                <building-gallary 
                                    ref="buildings" 
                                    gallaryRef="buildingsGallary" 
                                    :images_src="[require('@/assets/images/cat-no-photo-yet-green-2.jpg')]" 
                                    caption="Кошечка лучше, чем ничего"
                                >
                                </building-gallary>
                            </div> -->
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
// import vHeaderLittle from '../components/v-header-little'
import HighwayIcon from 'vue-material-design-icons/Highway.vue';
import HouseEditIcon from 'vue-material-design-icons/HomeEdit';
import HomeCityIcon from 'vue-material-design-icons/HomeCity';
import HomeGroupIcon from 'vue-material-design-icons/HomeGroup';
import DomainIcon from 'vue-material-design-icons/Domain';
import ClipboardCheckMultipleIcon from 'vue-material-design-icons/ClipboardCheckMultiple';
import KeyboardBackspaceIcon from 'vue-material-design-icons/KeyboardBackspace'
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
        // vHeaderLittle,
        HighwayIcon,
        HouseEditIcon,
        HomeCityIcon,
        HomeGroupIcon,
        DomainIcon,
        ClipboardCheckMultipleIcon,
        KeyboardBackspaceIcon
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
            if (this.building_images.length > 0){
                this.$refs.buildings.$refs.buildingsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
            }
            else if(this.layout_images.length > 0){
                this.$refs.layouts.$refs.layoutsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
            }
            else{
                this.$refs.buildings.$refs.buildingsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
            }
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
