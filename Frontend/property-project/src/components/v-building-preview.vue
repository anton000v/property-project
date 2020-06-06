<template>
    <modal 
    :name="'building-preview:'+building.slug"
    :width="900"
    :height="600"
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

        <div class="absolute inset-x-0 bottom-0 items-center text-center bg-gray-300 py-6">
            <router-link :to="{name:'building-page', params:{slug:slug}}">
            <p class=""> Открыть полностью </p>
            </router-link>
        </div>
    </modal>
</template>

<script>
export default {
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
