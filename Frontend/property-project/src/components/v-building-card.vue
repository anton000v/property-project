<template>
    <!-- <router-link :to="{
      name: 'building-page',
      params: {
        slug:building.slug
        } 
      }" 
      > -->
    <div id='modal-wrapper'>
      <!-- {{ isMouseOver }} -->
      <div @mouseover="isMouseOver=true" @mouseleave="isMouseOver = false" >
        <div class="hover:flex max-w-sm transition rounded-lg duration-500 ease-in-out hover:rounded-none hover:opacity-40 transform hover:-translate-y-1 sm:hover-scale-100 md:hover:scale-105 hover:shadow-2xl overflow-hidden shadow-lg">
          <img v-if="building.building_images[0]" :src="building.building_images[0].building_image" alt="">
          <p v-else>Нету изображения :р</p>
          <div class="flex items-center px-6 py-3 bg-gray-900">
              <!-- <svg class="h-6 w-6 text-white fill-current" viewBox="0 0 512 512">
                  <path d="M256 48C150 48 64 136.2 64 245.1v153.3c0 36.3 28.6 65.7 64 65.7h64V288h-85.3v-42.9c0-84.7 66.8-153.3 149.3-153.3s149.3 68.5 149.3 153.3V288H320v176h64c35.4 0 64-29.3 64-65.7V245.1C448 136.2 362 48 256 48z"/>
              </svg> -->
              <h1 class="mx-3 text-white font-semibold text-lg">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</h1>
          </div>
          <div class="px-6 py-4">
            <div class="mt-6 grid m-auto sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 justify-center text-center">
                <div class>
                  <p class="text-gray-700 font-bold">{{ building.administrative_district }}
                  </p>
                  <p class="text-md mt-2 text-gray-600 font-hairline">Административный район
                  </p>
                </div>
                <div>
                  <p class="text-gray-700 font-bold">{{ building.district }}
                  </p>
                  <p class="text-md mt-2 text-gray-600 font-hairline">Район
                  </p>
                </div>
                <div>
                  <p class="text-gray-700 font-bold">{{ building.developer }}
                  </p>
                  <p class="text-xs mt-2 text-gray-700 font-hairline">Застройщик
                  </p>
                </div>
            </div>
          </div>
          
          <!-- <div v-show="isMouseOver"> -->
          <div class="invisible md:visible">
            <transition name="preview">
              <div v-show="isMouseOver">
                <div class="flex flex-wrap opacity-75 absolute bottom-0 w-full left-0 bg-gray-200 h-full">
                    <div class="w-full h-1/2 bg-gray-500 hover:bg-gray-600 text-white">
                      <router-link :to="{name:'building-page', params:{slug:building.slug}}">
                        <div class='bg-black h-full'>     
                            Открыть полностью
                        </div>
                      </router-link>
                    </div>
                    <div class="w-full h-1/2 bg-gray-500 hover:bg-gray-600 text-white cursor-pointer" @click.prevent="show">Предпросмотр</div>
                </div>
              </div>
                <!-- <button class="object w-full">Предпросмотр</button> -->
                <!-- <button :class="[isMouseOver? 'visible' : '' , ' object w-full']">Предпросмотр</button> -->
              
            </transition>

          </div>
          <div class="visible md:invisible ">
            <router-link :to="{name:'building-page', params:{slug:building.slug}}">
              <div class="flex flex-wrap absolute bottom-0 w-full left-0 h-full cursor-pointer">
              </div>
            </router-link>
          </div>
        </div>
      </div>
      <!-- <modal :name="'building-preview:'+building.slug"> -->
        <vBuildingPreview :slug="building.slug" :building="building"/>
      <!-- </modal> -->
    </div>
    <!-- </router-link> -->

</template>

<script>
import vBuildingPreview from '../components/v-building-preview'

export default {
  props: {
      building: {
        type: Object,
      }, 
  },
  data(){
    return {
      isMouseOver: false
    }
  },
  components:{
    vBuildingPreview,
  },

  methods: {
    show () {
        this.$modal.show('building-preview:'+this.building.slug);
    },
    hide () {
        this.$modal.hide('building-preview:'+this.building.slug);
    },
  },
  // methods: {
  //   getSrc(imgPath) {
  //       return this.baseBackendAddress + imgPath
  //   }
  // }
}
</script>

<style scoped>

.preview-enter-active {
  transition: all .2s ease;
}
.preview-leave-active {
  transition: all .2s 
}
.preview-enter, .preview-leave-to
/* .slide-fade-leave-active до версии 2.1.8 */ {
  transform: translateX(100px);
  opacity: 0;
}



</style>