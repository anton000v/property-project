<template>
    <!-- <router-link :to="{
      name: 'building-page',
      params: {
        slug:building.slug
        } 
      }" 
      > -->
    <div id='modal-wrapper'>
      <div @mouseover="isMouseOver=true" @mouseleave="isMouseOver = false" >
        <div class="bg-white hover:flex max-w-sm transition rounded-lg duration-500 ease-in-out hover:rounded-none hover:opacity-40 transform md:hover:-translate-y-3 sm:hover:scale-100 md:hover:scale-100 hover:shadow-2xl overflow-hidden shadow-lg">
          <img v-if="flat.flat_images[0]" :src="flat.flat_images[0].flat_image" alt="">
          <img v-else-if="flat.flat_layouts[0]" :src="flat.flat_layouts[0].flat_layout" alt="">
          <img v-else :src="require('@/assets/images/no-photo-yet.jpg')" alt="Пока что нет фото :(">
          <div class="flex items md:px-2 py-1 md:py-3 bg-gray-900">
              <h1 class="mx-3 text-white font-semibold text-base">{{ flat.building.street }} {{ flat.building.house_number }}{{ flat.building.house_letter }}</h1>
          </div>
          <!-- <div class="hidden md:block md:py-4 m-1">
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
          </div> -->
            <div class="grid grid-col-1  py-2 m-1">

              <!-- <div v-if="building.administrative_district != null" class="inline-flex items-center">
                <HomeCityIcon class="text-myHeaderColor" :size="17"  />
                <div class="flex-1 sm:px-1 px-2 ">
                  Админ. район: <span class="font-bold">{{ building.administrative_district }}</span> 
                </div>
              </div>
              <div v-if="building.district != null" class="inline-flex items-center">
                <HomeGroupIcon class="text-myHeaderColor" :size="17" />
                <div class="flex-1 sm:px-1 px-2 ">
                  Район:  <span class="font-bold">{{ building.district }}</span> 
                </div>
              </div>
              <div v-if="building.micro_district !== 'Не делится на микрорайоны'" class="inline-flex items-center">
                <DomainIcon class="text-myHeaderColor" :size="17" />
                <div class="flex-1 sm:px-1 px-2 ">
                  Микрорайон:  <span class="font-bold">{{ building.micro_district }}</span> 
                </div>
              </div>
              <div v-if="building.developer != null" class="inline-flex items-center">
                <HouseEditIcon class="text-myHeaderColor" :size="17" />
                <div class="flex-1 sm:px-1 px-2 ">
                  Застройщик:  <span class="font-bold">{{ building.developer }}</span> 
                </div>
              </div> -->

            <div v-if="flat.building.administrative_district != null" class="inline-flex items-center">
                <HomeCityIcon class="text-myHeaderColor" :size="20"  />
                <div class="flex-1 sm:px-1 px-2 text-sm">
                  Адресс: <span class="font-bold text-myHeaderColor">
                      Харьков
                    <span v-if="flat.building.administrative_district != null">, {{ flat.building.administrative_district}}</span>
                    <span v-if="flat.building.district != null">, {{flat.building.district}}</span>
                    <span v-if="flat.building.street != null">, {{ flat.building.street }}</span>
                    <span v-if="flat.building.house_number != null">, {{ flat.building.house_number }}</span>
                    <span v-if="flat.building.house_letter != null">, {{ flat.building.house_letter }}</span>
                    </span> 
                </div>
            </div>
            <div v-if="flat.building.developer != null" class="inline-flex items-center">
                <HouseEditIcon class="text-myHeaderColor" :size="20" />
                <div class="flex-1 sm:px-1 px-2 text-sm">
                    Застройщик:  <span class="font-bold text-myHeaderColor">{{ flat.building.developer }}</span> 
                </div>
            </div>
            <div v-if="flat.rooms != null" class="inline-flex items-center">
                <DoorIcon class="text-myHeaderColor" :size="20" />
                <div class="flex-1 sm:px-1 px-2 text-sm">
                    Комнат:  <span class="font-bold text-myHeaderColor">{{ flat.rooms }}</span> 
                </div>
            </div>
            <div v-if="flat.floor != null" class="inline-flex items-center">
                <HomeFloor0Icon class="text-myHeaderColor" :size="20" />
                <div class="flex-1 sm:px-1 px-2 text-sm">
                  Этаж / этажность:  <span class="font-bold text-myHeaderColor">{{ flat.floor }}/{{ flat.building.number_of_storeys }}</span> 
                </div>
            </div>

            <div v-if="flat.living_area != null" class="inline-flex items-center">
                <RulerIcon class="text-myHeaderColor" :size="20" />
                <div class="flex-1 sm:px-1 px-2 text-sm">
                    S общ/жил/кух:  
                    <span class="font-bold text-myHeaderColor" v-if="flat.kitchen_area">{{ flat.living_area + flat.kitchen_area }}/{{ flat.living_area }}/{{ flat.kitchen_area }}</span>
                    <span class="font-bold text-myHeaderColor" v-else>{{ flat.living_area }}/{{ flat.living_area }}/-</span>
                    м<sup>2</sup>
                </div>
            </div>
                <div v-if="flat.price != null" class="inline-flex items-center">
                    <p class="font-bold text-myMint-400 px-4 pt-2">{{ flat.price }}$</p>
                </div>
            </div>
          <div class="invisible md:visible">
               <TransitionSlowAppearance>
                <div v-show="isMouseOver">
                    <div id="action-choice-container" class="flex flex-wrap  absolute bottom-0 w-full left-0 h-full">
                        <div class="my-action-choice w-full h-1/2 text-white">
                          <router-link :to="{name:'flat-page', params:{slug:flat.building.slug, id:flat.id}}">
                            <div class='flex h-full'>     
                              <div class="m-auto text-xl">
                                Открыть полностью
                              </div>
                            </div>
                          </router-link>
                        </div>
                        <div class="my-action-choice w-full h-1/2 text-white cursor-pointer" @click.prevent="$emit('show', flat)">
                            <div class='flex h-full'>     
                              <div class="m-auto text-xl">
                                Предпросмотр
                              </div>
                            </div>
                        </div>

                  </div>
           </div>
            </TransitionSlowAppearance>
          </div>
          <div class="visible md:invisible ">
            <router-link :to="{name:'flat-page', params:{slug:flat.building.slug, id:flat.id}}">
              <div class="flex flex-wrap absolute bottom-0 w-full left-0 h-full cursor-pointer">
              </div>
            </router-link>
          </div>
        </div>
      </div>
        <!-- <vFlatPreview :slug="flat.building.slug" :flat="flat"/> -->
    </div>

</template>

<script>
// import vFlatPreview from '../components/v-flat-preview'
import TransitionSlowAppearance from '../transitions/slowAppearance'
import HouseEditIcon from 'vue-material-design-icons/HomeEdit';
import HomeCityIcon from 'vue-material-design-icons/HomeCity';
import DoorIcon from 'vue-material-design-icons/Door'
import HomeFloor0Icon from 'vue-material-design-icons/HomeFloor0'
import RulerIcon from 'vue-material-design-icons/Ruler'
// import HomeGroupIcon from 'vue-material-design-icons/HomeGroup';
// import DomainIcon from 'vue-material-design-icons/Domain';

export default {
  props: {
    //   building: {
    //     type: Object,
    //   }, 
      flat: {
          type: Object
      }
  },
  data(){
    return {
      isMouseOver: false
    }
  },
  components:{
    // vFlatPreview,
    TransitionSlowAppearance,
    HouseEditIcon,
    HomeCityIcon,
    DoorIcon,
    HomeFloor0Icon,
    RulerIcon
    // HomeGroupIcon,
    // DomainIcon,
  },

  methods: {
    // show () {
    //     this.$modal.show(`flat-preview:${this.flat.building.slug}-${this.flat.id}`);
    // },
    // hide () {
    //     this.$modal.hide(`flat-preview:${this.flat.building.slug}-${this.flat.id}`);
    // },
  },

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