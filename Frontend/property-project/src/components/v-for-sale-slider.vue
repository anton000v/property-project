
<template>
  <div class="">

    <swiper class="swiper my-20" :options="swiperOption">

        <swiper-slide
          v-for="flat in flats"
          :key="flat.id"
          class="my-20 rounded-lg"
        >
          <vFlatsSliderCard @show="show"  :flat="flat"/>
        </swiper-slide>

      <!-- <div class="swiper-pagination" slot="pagination"></div> -->
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
      <vFlatPreview v-for="flat in flats" :key="flat.id" :slug="flat.building.slug" :flat="flat"/>
  </div>
</template>

<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  // import vFlatCard from './v-flat-card.vue'
  import { baseApiAddress } from '../variables'
  import vFlatsSliderCard from './v-flats-slider-card'
  import vFlatPreview from './v-flat-preview'
  // import 'swiper/css/swiper.css'

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
      vFlatsSliderCard,
      vFlatPreview
    },
    data() {
      return {
        swiperOption: {

          slidesPerView: 3,
          centeredSlides: true,
          spaceBetween: 30,

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
    },
    methods: {
      show (flat) {
        this.$modal.show(`flat-preview:${flat.building.slug}-${flat.id}`);
      },
      hide (flat) {
          this.$modal.hide(`flat-preview:${flat.building.slug}-${flat.id}`);
      },
    }
  }
</script>

<style lang="scss" scoped>

    .content {
      width: 100%;
    }
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