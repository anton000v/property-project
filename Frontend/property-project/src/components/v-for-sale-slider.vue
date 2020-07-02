
<template>
  <div class="">

    <swiper class="swiper" :options="swiperOption">
      <swiper-slide
        v-for="flat in flats"
        :key="flat.id"
      >
        <v-flat-card class=" overflow-visible" :flat="flat"/>
      </swiper-slide>
      <!-- <div class="swiper-pagination" slot="pagination"></div> -->
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import vFlatCard from './v-flat-card.vue'
  import { baseApiAddress } from '../variables'
  import 'swiper/css/swiper.css'

  export default {
    props:{
      flatsIdForSale:{
        type: Array,
        required: true
      },
    },
    components: {
      Swiper,
      SwiperSlide,
      vFlatCard
    },
    data() {
      return {
        swiperOption: {

          slidesPerView: 3,
          centeredSlides: true,
          spaceBetween: 30,
          freeMode:true,
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          },
        },
        flats: []
      }
    },
    async mounted() {
          const axios = require('axios');

          this.flatsIdForSale.forEach(async (flat) => {
            
            await axios.get(baseApiAddress+'flats/'+flat.id, {
            // params: {
            //     slug:this.$route.params.slug
            //     }
            }).then(resp => {
            this.flats.push(resp.data)
            })
            // console.log(this.building)
          })
    }
    // methods: {
    //   appendSlide() {
    //     this.swiperSlides.push(this.swiperSlides.length + 1)
    //   },
    //   prependSlide() {
    //     this.swiperSlides.unshift(this.swiperSlides[0] - 1)
    //   },
    //   popSlide() {
    //     this.swiperSlides.pop()
    //   },
    //   shiftSlide() {
    //     this.swiperSlides.shift()
    //   }
    // }
  }
</script>

<style lang="scss" scoped>
  // @import './base.scss';

  // .example {
  //   height: auto;

  //   .toolbar {
  //     display: flex;
  //     justify-content: space-around;
  //     width: 100%;
  //     height: 2rem;
  //     border-bottom: 1px solid $body-bg;
  //     margin-bottom: $gap;

  //     button {
  //       flex: 1;
  //       padding: 0;
  //       margin: 0;
  //       border: none;
  //       border-right: 1px solid $body-bg;
  //       background-color: $module-bg;
  //       cursor: pointer;
  //       &:last-child {
  //         border: none;
  //       }

  //       &:hover {
  //         background-color: $module-bg-darken;
  //       }
  //     }
  //   }
  // }
</style>