<template>
    <modal 
    :name="'building-preview:'+building.slug"
    :width="modalWidth"
    :height="modalHeight"
    :adaptive="true"
    
    >
        <div slot="top-right" class="py-8 px-8">
            <button @click="$modal.hide('building-preview:'+building.slug)">
                <!-- <div class="modal-close absolute top-0 right-0 cursor-pointer flex flex-col items-center mt-4 mr-4 text-white text-sm z-50"> -->
                    <svg class="opacity-50 fill-current text-myFirstLight" xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 18 18">
                        <path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
                    </svg>
                    <!-- <span class="text-sm">(Esc)</span> -->
                <!-- </div> -->
            </button>
        </div>

        <div class="items-center text-center w-full">
            <div class="grid md:grid-cols-2 justify-center">
                <div class="flex h-16">
                    <p class="m-auto text-2xl font-bold">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
                </div>
                <router-link :to="{name:'building-page', params:{slug:slug}}">
                    <!-- <div class="flex h-16 shadow-md bg-myFirstLight hover:shadow-xl "> -->
                    <div class="flex h-16 bg-myFirstLight transition duration-500 ease-in-out hover:rounded-none hover:opacity-40 transform hover:translate-y-1 hover:shadow-2xl overflow-hidden shadow-md">  
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
        <div v-else>
            <p>Пока нет фотографий!</p>
        </div>
        <div>  
            <div class= 'h-full w-full px-10 py-4'>
                <!-- <div class='flex justify-center'> -->
                <div class="flex justify-center text-center">
                    <!-- <div>
                        <highway-icon :size="48" />
                    </div> -->
                    <div class="flex-1 flex-col bg-gray-200 ">
                        <div class="flex-1 text-gray-700 font-bold text-center bg-gray-400 px-4 py-2 m-2">Административный район</div>
                        <div class="flex-1 text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.administrative_district }}</div>
                    </div>
                    <div class="flex-1 flex-col bg-gray-200 ">
                            <div class="flex-1 text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-2">Район</div>
                            <div class="flex-1 text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.district }}</div>
                    </div>
                    <div v-if="building.micro_district !== 'Не делится на микрорайоны'" class="flex-1 flex-col bg-gray-200 ">
                            <div class="flex-1 text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-2">Микрорайон</div>
                            <div class="flex-1 text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.micro_district }}</div>
                    </div>
                    <div class="flex-1 flex-col bg-gray-200 ">
                            <div class="flex-1 text-gray-700 font-bold  text-center bg-gray-400 px-4 py-2 m-2">Застройщик</div>
                            <div class="flex-1 text-gray-700 text-center bg-gray-400 px-4 py-2 m-2">{{ building.developer }}</div>
                    </div>
                </div>
                    <div class="flex flex-col bg-gray-200 my-3">
                        <div class="flex-1 text-gray-700 text-center font-bold  bg-gray-400 px-4 py-2 m-2">Пути от метро <span><highway-icon :size="40" /></span> </div>
                    <div class="flex-1 text-gray-700 text-center bg-gray-400 px-4 py-2 m-2"></div>
                </div>
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
//local registration
// import {VueTabs, VTab} from 'vue-nav-tabs/dist/vue-tabs.js'
//you can also import this in your style tag
// import 'vue-nav-tabs/themes/vue-tabs.css'
export default {
    components:{
        vPreviewSlider,
        HighwayIcon
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
        }
    },
}
</script>

<style scoped>
    /* .vm--overlay {
    background: red;
    } */
</style>

