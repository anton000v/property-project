<template>
    <modal 
    :name="'building-preview:'+building.slug"
    :width="modalWidth"
    :height="modalHeight"
    :adaptive="true"
    :scrollable="true"
    
    >
        <!-- <div slot="top-right" class="py-8 px-8">
            <button @click="$modal.hide('building-preview:'+building.slug)">
                    <svg class="opacity-50 fill-current text-myFirstLight" xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 18 18">
                        <path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
                    </svg>
            </button>
        </div> -->
        <div class="bg-myPageBackground">
            <div class="items-center text-center w-full">
                <div class="grid md:grid-cols-2 justify-center">
                    <div class="flex h-16">
                        <p class="m-auto text-2xl font-bold">{{fullBuildingAddress}}</p>
                    </div>
                    <router-link :to="{name:'building-page', params:{slug:slug}}">
                        <!-- <div class="flex h-16 shadow-md bg-myFirstLight hover:shadow-xl "> -->
                        <div class="flex h-16 bg-myHeaderColor text-white hover:bg-myMint-400 transition duration-500 ease-in-out hover:rounded-none hover:opacity-40 transform hover:translate-y-1 hover:shadow-2xl overflow-hidden shadow-md">  
                            <p class="m-auto text-xl"> Открыть полностью </p>
                        </div>
                    </router-link>
                </div>
            </div>
            <!-- <div class=''>   -->
            <div id='preview-slider' class='py-2 h-screen/2' v-if="sliderImages.length">
                <vPreviewSlider 
                :images="sliderImages" 
                />
            </div>
            <div id='preview-slider' class='py-2 h-screen/2' v-else>
                <vPreviewSlider 
                    :images="[require('@/assets/images/no-photo-yet.jpg')]" 
                />
            </div>
            <div class="pr-5 pl-5 pb-5"> 
                 <!-- <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"> -->
                            <!-- <div class="px-1 md:px-4 py-5 flex-auto">
                                <div class="text-2xl">
                                    <p class="uppercase font-bold text-gray-700">ЖК {{ building.name }}</p>
                                    <p class="text-gray-700 font-bold">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
                                </div>
                                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-6 pt-6">
                                    <div class="">
                                        <img v-if="building.building_images[0]" :src="building.building_images[0].building_image" class="cursor-pointer" @click="openMainImage"  alt="Главное фото">
                                        <img v-else-if="building.layout_images[0]" :src="building.layout_images[0].layout_image" class="cursor-pointer" @click="openMainImage"  alt="Главное фото">
                                        <img v-else :src="require('@/assets/images/cat-no-photo-yet-green-2.jpg')" class="cursor-pointer" @click="openMainImage" alt="Главное фото">
                                    </div>
                                    <div class="col-span-1"> -->
                                        <div class= 'w-full'>
                                            <div class="flex justify-end m-2 relative">
                                                <!-- <div class="border rounded-lg border-myMint-400 text-gray-700 text-xl px-4 py-2">
                                                </div> -->
                                                <vShareDropdown :pageUrl="pageUrl" :descriptionText="fullBuildingAddress"/>
                                            </div>
                                            <div class="flex justify-center justify-center text-center justify-center gap-2">
                                                <div v-if="building.administrative_district != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center text-wh">
                                                            <HomeCityIcon class="text-myMint-400" :size="30"  />
                                                            <div class="block xl:hidden flex-1 px-1  ">
                                                                Админ. район
                                                            </div>
                                                            <div class="hidden xl:block flex-1 px-2  ">
                                                                Административный район
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="rounded-lg bg-gray-200  text-gray-700 text-base md:text-lg text-center md:px-4 py-2 m-2">{{ building.administrative_district }}</div>
                                                </div>
                                                <div v-if="building.district != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <HomeGroupIcon class="text-myMint-400" :size="30" />
                                                            <div class="flex-1 sm:px-1 px-2">
                                                                Район
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="rounded-lg bg-gray-200 text-gray-700 text-base md:text-lg text-center md:px-4 py-2 m-2">{{ building.district }}</div>
                                                </div>
                                                <div v-if="building.micro_district !== 'Не делится на микрорайоны'" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <DomainIcon class="text-myMint-400" :size="30" />
                                                            <div class="flex-1 sm:px-1 px-2">
                                                                Микрорайон
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="bg-gray-200 rounded-lg text-gray-700 text-base md:text-lg  text-center md:px-4 py-2 m-1 md:m-2">{{ building.micro_district }}</div>
                                                </div>
                                                <div v-if="building.developer != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <HouseEditIcon class="text-myMint-400" :size="30" />
                                                            <div class="flex-1 sm:px-1 px-2">
                                                                Застройщик
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="bg-gray-200 rounded-lg text-gray-700 text-base md:text-lg text-center  md:px-4 py-2 m-2">{{ building.developer }}</div>
                                                </div>
                                            </div>
                                            <div v-if="building.ways_from_metro != null && building.ways_from_metro.length > 0" class=" rounded-lg  mt-5 shadow-sm md:transition md:duration-500 md:hover:shadow-md" >
                                                <div class="px-2 py-2">
                                                    <div class="text-gray-700 text-base text-center">
                                                        <div class="inline-flex items-center">
                                                            <highway-icon class="text-myMint-400" 
                                                             />
                                                            <div class="flex-1 m-1 md:m-2 px-4 p-2">
                                                                Пути от метро
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="flex-1 text-center">
                                                        <div class="w-full rounded-lg bg-gray-200 text-gray-700 text-base md:text-lg flex justify-center mt-2 lg:px-4 pb-2 pt-2" v-for="way in building.ways_from_metro" :key="way.metro">
                                                            <div class="w-2/5"> {{ way.metro }} </div>
                                                            <div class="w-1/5"> {{ way.type_of_movement }} </div>
                                                            <div class="w-1/5"> {{ way.time }} мин. </div>
                                                            <div class="w-1/5"> {{ way.number_of_meters }} м. </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- <div v-if="building.completion_date != null" class="flex1 rounded-lg mt-5 shadow-sm md:transition md:duration-500 md:hover:shadow-md" >
                                               <div class="px-2 py-2">
                                                <div class="text-gray-700 text-base text-center px-4 py-2 m-2">
                                                    <div class="inline-flex items-center">
                                                        <ClipboardCheckMultipleIcon class="text-myMint-400" :size="30" />
                                                        <div class="flex-1 px-2">
                                                            Сдан в эксплуатацию
                                                        </div>
                                                    </div>
                                                </div>
                                                    <div class="rounded-lg bg-gray-200 text-gray-700 text-base md:text-lg text-center md:px-4 py-2 ">{{ building.completion_date }}</div>
                                                </div>
                                            </div> -->
                                         </div>
                                    <!-- </div>
                                </div>
                            </div> -->
                        <!-- </div>  -->
                <!-- <div class= 'h-full w-full px-10 py-4'>
                    <div class="flex justify-center text-center">
                        <div class="flex-1 flex-col bg-gray-200 ">
                            <div class="text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-2">
                                <div class="inline-flex items-center">
                                    <HomeCityIcon :size="30" />
                                    <div class="flex-1 px-2">
                                        Административный район
                                    </div>
                                </div>
                            </div>
                            <div class="flex-1 text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.administrative_district }}</div>
                        </div>
                        <div class="flex-1 flex-col bg-gray-200 ">
                            <div class="text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-2">
                                <div class="inline-flex items-center">
                                    <HomeGroupIcon :size="30" />
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
                                        <DomainIcon :size="30" />
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
                                        <HouseEditIcon :size="30" />
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
                                    <highway-icon :size="30" />
                                    <div class="flex-1 my-2 px-4 py-2">
                                        Пути от метро
                                    </div>
                                </div>
                            </div>

                            
                            <div class="flex-1 text-gray-700 text-center bg-gray-400 ">
                                <div class="w-full flex justify-center my-2 px-4 py-2" v-for="way in building.ways_from_metro" :key="way.metro">
                                    <div class="w-1/4"> {{ way.metro }} </div>
                                    <div class="w-1/4"> {{ way.type_of_movement }} </div>
                                    <div class="w-1/4"> {{ way.time }} мин. </div>
                                    <div class="w-1/4"> {{ way.number_of_meters }} м. </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div> -->
            </div>
        </div>
        <!-- </div> -->
    <!-- <vue-tabs
    active-tab-color="#e74c3c" 
    active-text-color="white"
    type="pills"
    text-position="bottom"
    centered
    :name="slug"
    >


        <v-tab :name="slug+'-images'" :id="slug+'-images'" title="Изображения">
            
            
            <vPreviewSlider :images="building.building_images" :slug="slug" field_name="building_image"/>
        </v-tab>

        <v-tab :name="slug+'-layouts'" :id="slug+'-layouts'" title="Планировки">
            
            <vPreviewSlider :images="building.layout_images" :slug="slug" field_name="layout_image"/>
        </v-tab> 
    </vue-tabs> -->

<!-- </div> -->

        <!-- <v-tab :prefix="building.slug+'-'" title="Изображения">
            <vPreviewSlider :images="building.building_images" field_name="building_image"/>
        </v-tab>

        <v-tab :prefix="building.slug+'-'" title="Планировки">
            tratataa
            <vPreviewSlider :images="building.layout_images" field_name="layout_image"/>
        </v-tab>  -->
        <!-- <div>
            <vPreviewSlider :images="building.building_images" field_name="building_image"/>
        </div> -->

        <!-- <div class="relative inset-x-0 bottom-0 items-center text-center bg-gray-300">
            <router-link :to="{name:'building-page', params:{slug:slug}}">
                <p class=""> Открыть полностью </p>
            </router-link>
            </div> -->

    </modal>
</template>

<script>
import vPreviewSlider from './v-preview-slider'
import HighwayIcon from 'vue-material-design-icons/Highway.vue';
import HouseEditIcon from 'vue-material-design-icons/HomeEdit';
import HomeCityIcon from 'vue-material-design-icons/HomeCity';
import HomeGroupIcon from 'vue-material-design-icons/HomeGroup';
import DomainIcon from 'vue-material-design-icons/Domain';
import vShareDropdown from './v-share-dropdown'
export default {
    components:{
        vPreviewSlider,
        HighwayIcon,
        HouseEditIcon,
        HomeCityIcon,
        HomeGroupIcon,
        DomainIcon,
        vShareDropdown
        // VueTabs,
        // VTab
    },
    props:{
        slug: {
            type: String,
            }, 
        building: {
            type: Object,
        }
    },
    methods: {

    },
    data(){
        return{
            modalWidth:1000,
            // modalHeight:800,
            modalHeight:'auto'
        }
    },
    computed: {
        sliderImages: function (){
            let images = []
            this.building.building_images.forEach(function(entry) {
                images.push(entry.building_image)
            });
            this.building.layout_images.forEach(function(entry) {
                images.push(entry.layout_image)
            });
            return images
        },
        pageUrl: function(){ 
            let url = this.$router.resolve({ 
                name: 'building-page',
                params: { slug:this.building.slug},
            }).href
            return window.location.origin + "/" + url
        },
        fullBuildingAddress: function(){
            let house_letter = this.building.house_letter != null ? this.building.house_letter : ''
            // alert(house_letter)
            // console.log(house_letter)
            return this.building.street + ' ' + this.building.house_number + house_letter
        },
    },
}
</script>

<style scoped>
    /* .vm--overlay {
    background: red;
    } */
</style>

