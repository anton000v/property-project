<template>
    <modal 
    :name="'building-preview:'+building.slug"
    :width="1000"
    :height="700"
    :adaptive="true"
    :draggable="true"
    >
        <!-- <div id="modal-header" class="bg-gray-300"> -->
            <div class="bg-gray-300 items-center text-center w-full py-6">
                <p class="text-2xl font-bold">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
            </div>
        <!-- </div> -->
        
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

<!-- <div :class="'wrapper' "> -->
    <vue-tabs
    active-tab-color="#e74c3c" 
    active-text-color="white"
    type="pills"
    text-position="bottom"
    centered
    :name="slug"
    >

    <!-- <vPreviewSlider :images="building.building_images" field_name="building_image"/> -->

        <v-tab :id="slug+'-images'" title="Изображения">
            
            <!-- lalalala -->
            <vPreviewSlider :images="building.building_images" :slug="slug" field_name="building_image"/>
        </v-tab>

        <v-tab :id="slug+'-layouts'" title="Планировки">
            tratataa
            <vPreviewSlider :images="building.layout_images" :slug="slug" field_name="layout_image"/>
        </v-tab> 

    <!-- <v-tab title="Third tab">
      Third tab content
    </v-tab> -->
    </vue-tabs>
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

        <div class="absolute inset-x-0 bottom-0 items-center text-center bg-gray-300 py-6">
            <router-link :to="{name:'building-page', params:{slug:slug}}">
            <p class=""> Открыть полностью </p>
            </router-link>
        </div>
    </modal>
</template>

<script>
import vPreviewSlider from './v-preview-slider'
//local registration
import {VueTabs, VTab} from 'vue-nav-tabs/dist/vue-tabs.js'
//you can also import this in your style tag
import 'vue-nav-tabs/themes/vue-tabs.css'
export default {
    components:{
        vPreviewSlider,
        VueTabs,
        VTab
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
}
</script>

<style scoped >

</style>