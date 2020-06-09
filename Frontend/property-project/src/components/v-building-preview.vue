<template>
    <modal 
    :name="'building-preview:'+building.slug"
    :width="modalWidth"
    :height="modalHeight"
    :adaptive="true"
    :draggable="true"
    >
        <div slot="top-right">
            <button @click="$modal.hide('building-preview:'+building.slug)">
                <!-- <div class="modal-close absolute top-0 right-0 cursor-pointer flex flex-col items-center mt-4 mr-4 text-white text-sm z-50"> -->
                    <svg class="fill-current text-black" xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 18 18">
                    <path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
                    </svg>
                    <span class="text-sm">(Esc)</span>
                <!-- </div> -->
            </button>
        </div>

        <div class="bg-gray-300 items-center text-center w-full">
            <div class="grid md:grid-cols-2 justify-center">
                <div class="flex h-16 bg-blue-500">
                    <p class="m-auto text-2xl font-bold">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
                </div>
                <router-link :to="{name:'building-page', params:{slug:slug}}">
                    <div class="flex h-16 bg-red-500">
                        <p class="m-auto text-xl font-bold"> Открыть полностью </p>
                    </div>
                </router-link>
            </div>
        </div>
        <!-- <div class=''>   -->
            <div id='preview-slider' class='h-screen/2'>
                <vPreviewSlider 
                :images="sliderImages" 

                />
            </div>
            <div>  
                <div class= 'h-full w-full px-10 py-4'>
                    <div class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 justify-center gap-4">
                        <div>
                            <highway-icon :size="48" />
                        </div>
                        <div>
                            asdasd
                        </div>
                        <div>
                            asfsdgsdgdsfh
                        </div>
                        <div>
                            asfdasdfsadfsdfds
                        </div>
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

