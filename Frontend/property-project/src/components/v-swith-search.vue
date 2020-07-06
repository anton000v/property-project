<template>
    <div class="flex my-2">
        <div class="w-full md:w-1/3">
        <router-link :to="{name:'search-buildings'}">
            <div  class=" h-full group bg-myHeaderColor border flex rounded-full cursor-pointer transition duration-500 transform hover:translate-y-1 hover:shadow-xl" :class="{'border-myOrange':$route.name=='search-buildings'}">
                <div class="m-auto">
                <div class="flex"> 
                    <GoogleMapsIcon class="m-auto text-white transition duration-500 group-hover:text-myMint-300"/>
                    <p class="text-white pl-2 text-base p-2">Обычный поиск</p>
                </div>
                </div>
            </div>
            </router-link>
        </div>
        <div class="w-full md:w-1/3">
            <router-link :to="{name:'map-search'}">
            <div  class=" h-full group bg-myHeaderColor border flex rounded-full cursor-pointer transition duration-500 transform hover:translate-y-1 hover:shadow-xl" :class="{'border-myOrange':$route.name=='map-search'}">
                <div class="m-auto">
                <div class="flex"> 
                    <GoogleMapsIcon class="m-auto text-white transition duration-500 group-hover:text-myMint-300"/>
                    <p class="text-white pl-2 text-base p-2">Поиск по карте</p>
                </div>
                </div>
            </div>
            </router-link>
        </div>

    </div>
</template>

<script>
import GoogleMapsIcon from 'vue-material-design-icons/GoogleMaps';
export default {
    components:{
        GoogleMapsIcon
    }
}
</script>