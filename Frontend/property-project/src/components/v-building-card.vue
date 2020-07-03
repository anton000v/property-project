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
        <div class="bg-white hover:flex max-w-sm transition rounded-lg duration-500 ease-in-out hover:rounded-none hover:opacity-40 transform md:hover:-translate-y-3 sm:hover:scale-100 md:hover:scale-100 hover:shadow-2xl overflow-hidden shadow-lg">

          <div v-if="building.flats_for_sale.length > 0" class="absolute px-2 m-2 rounded-full bg-myOrange font-bold text-white p-1 text-xs">{{building.flats_for_sale.length }} в продаже</div>

          <img v-if="building.building_images[0]" :src="building.building_images[0].building_image" alt="">
          <img v-else-if="building.layout_images[0]" :src="building.layout_images[0].layout_image" alt="">
          <img v-else :src="require('@/assets/images/no-photo-yet.jpg')" alt="Пока что нет фото :(">
          <div class="flex items-center md:px-6 py-1 md:py-3 bg-gray-900">
              <!-- <svg class="h-6 w-6 text-white fill-current" viewBox="0 0 512 512">
                  <path d="M256 48C150 48 64 136.2 64 245.1v153.3c0 36.3 28.6 65.7 64 65.7h64V288h-85.3v-42.9c0-84.7 66.8-153.3 149.3-153.3s149.3 68.5 149.3 153.3V288H320v176h64c35.4 0 64-29.3 64-65.7V245.1C448 136.2 362 48 256 48z"/>
              </svg> -->
              <h1 class="mx-3 text-white font-semibold text-lg">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</h1>
          </div>
          <div class="hidden md:block md:py-4 m-1">
             <div class="grid grid-cols-2 justify-center text-center gap-2">
                <div v-if="building.administrative_district != null" class="flex-1 rounded-lg flex-col bg-gray-200 shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                    <div class="text-gray-700 text-base text-center px-2 py-2 m-1 md:m-2">
                        <div class="inline-flex items-center">
                            <HomeCityIcon class="text-myHeaderColor" :size="20"  />
                            <div class="flex-1 sm:px-1 px-2">
                                Админ. район
                            </div>
                        </div>
                    </div>
                    <div class="rounded-lg text-gray-700 text-base text-center md:px-4 py-2">{{ building.administrative_district }}</div>
                </div>
                <div v-if="building.district != null" class="flex-1 rounded-lg flex-col bg-gray-200 shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                    <div class="text-gray-700 text-base text-center px-2 py-2 m-1 md:m-2">
                        <div class="inline-flex items-center">
                            <HomeGroupIcon class="text-myHeaderColor" :size="20" />
                            <div class="flex-1 sm:px-1 px-2">
                                Район
                            </div>
                        </div>
                    </div>
                    <div class="rounded-lg text-gray-700 text-base text-center md:px-4 py-2">{{ building.district }}</div>
                </div>
                <div v-if="building.micro_district !== 'Не делится на микрорайоны'" class="flex-1 rounded-lg flex-col bg-gray-200 shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                    <div class="text-gray-700 text-base text-center px-2 py-2 m-1 md:m-2">
                        <div class="inline-flex items-center">
                            <DomainIcon class="text-myHeaderColor" :size="20" />
                            <div class="flex-1 sm:px-1 px-2">
                                Микрорайон
                            </div>
                        </div>
                    </div>
                    <div class=" rounded-lg text-gray-700 text-base text-center md:px-4 py-2">{{ building.micro_district }}</div>
                </div>
                <div v-if="building.developer != null" class="flex-1 rounded-lg flex-col bg-gray-200 shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                    <div class="text-gray-700 text-base text-center px-2 py-2 m-1 md:m-2">
                        <div class="inline-flex items-center">
                            <HouseEditIcon class="text-myHeaderColor" :size="20" />
                            <div class="flex-1 sm:px-1 px-2">
                                Застройщик
                            </div>
                        </div>
                    </div>
                    <div class=" rounded-lg text-gray-700 text-base text-center  md:px-4 py-2 ">{{ building.developer }}</div>
                </div>
            </div>
          </div>
            <div class="grid grid-col-1 block md:hidden py-2 m-1">
              <div v-if="building.administrative_district != null" class="inline-flex items-center">
                <HomeCityIcon class="text-myHeaderColor" :size="17"  />
                <div class="flex-1 sm:px-1 px-2 text-sm">
                  {{ building.administrative_district }}
                </div>
              </div>
              <div v-if="building.district != null" class="inline-flex items-center">
                <HomeGroupIcon class="text-myHeaderColor" :size="17" />
                <div class="flex-1 sm:px-1 px-2 text-sm">
                    {{ building.district }}
                </div>
              </div>
              <div v-if="building.micro_district !== 'Не делится на микрорайоны'" class="inline-flex items-center">
                <DomainIcon class="text-myHeaderColor" :size="17" />
                <div class="flex-1 sm:px-1 px-2 text-sm">
                    {{ building.micro_district }}
                </div>
              </div>
              <div v-if="building.developer != null" class="inline-flex items-center">
                <HouseEditIcon class="text-myHeaderColor" :size="17" />
                <div class="flex-1 sm:px-1 px-2 text-sm">
                    {{ building.developer }}
                </div>
              </div>
            </div>
          <!-- <div v-show="isMouseOver"> -->
          <div class="invisible md:visible">
             <!-- <transition name="preview"> -->
               <TransitionSlowAppearance>
                <div v-show="isMouseOver">
                
                  
                    <div id="action-choice-container" class="flex flex-wrap absolute bottom-0 w-full left-0  h-full">
                        <div class="my-action-choice w-full h-1/2  text-white">
                          <router-link :to="{name:'building-page', params:{slug:building.slug}}">
                            <div class='flex h-full'>     
                              <div class="m-auto text-xl">
                                Открыть полностью
                              </div>
                            </div>
                          </router-link>
                        </div>
                        <div class="my-action-choice w-full h-1/2  text-white cursor-pointer" @click.prevent="show">
                            <div class='flex h-full'>     
                              <div class="m-auto text-xl">
                                Предпросмотр
                              </div>
                            </div>
                        </div>
                    
                  </div>
                <!-- <button class="object w-full">Предпросмотр</button> -->
                <!-- <button :class="[isMouseOver? 'visible' : '' , ' object w-full']">Предпросмотр</button> -->
              
             
           </div>
            <!-- </transition> -->
            </TransitionSlowAppearance>
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
import TransitionSlowAppearance from '../transitions/slowAppearance'
import HouseEditIcon from 'vue-material-design-icons/HomeEdit';
import HomeCityIcon from 'vue-material-design-icons/HomeCity';
import HomeGroupIcon from 'vue-material-design-icons/HomeGroup';
import DomainIcon from 'vue-material-design-icons/Domain';

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
    TransitionSlowAppearance,
    HouseEditIcon,
    HomeCityIcon,
    HomeGroupIcon,
    DomainIcon,
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

#action-choice-container{
  background-color: rgba(25, 27, 29, 0.8);
}
.my-action-choice:hover{
  background-color: rgba(34, 31, 31, 0.8);
}

</style>