<template>
  <div class="">

    <swiper class="swiper my-20" :options="swiperOption">

      <swiper-slide
          v-for="flat in flats"
          :key="flat.id"
          class="my-20 rounded-lg"
      >
        <vFlatsSliderCard @show="show" :flat="flat"/>
      </swiper-slide>

      <!-- <div class="swiper-pagination" slot="pagination"></div> -->
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
    <vFlatPreview v-for="flat in flats" :key="flat.id" :slug="flat.building.slug" :flat="flat"/>
  </div>
</template>

<script>
import {Swiper, SwiperSlide} from 'vue-awesome-swiper'
// import vFlatCard from './v-flat-card.vue'
import {baseApiAddress} from '../variables'
import vFlatsSliderCard from './v-flats-slider-card'
import vFlatPreview from './v-flat-preview'
import 'swiper/css/swiper.css'

export default {
  props: {
    flatsIdForSale: {
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

        slidesPerView: 1,
        centeredSlides: true,
        spaceBetween: 30,

        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
          // 'hideOnClick': true
        },
        // Responsive breakpoints
        breakpoints: {
          // when window width is >= 320px
          320: {
            slidesPerView: 1,
            spaceBetween: 20
          },
          // when window width is >= 480px
          480: {
            slidesPerView: 1,
            spaceBetween: 30
          },
          // when window width is >= 640px
          640: {
            slidesPerView: 2,
            spaceBetween: 40
          },
          1024: {
            slidesPerView: 3,
            spaceBetween: 40
          }
        }
      },
      flats: []
    }
  },
  async mounted() {
    // const axios = require('axios');

    this.flatsIdForSale.forEach(async (flat) => {

      await this.$http.get(baseApiAddress + 'flats/' + flat.id, {
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
    show(flat) {
      this.$modal.show(`flat-preview:${flat.building.slug}-${flat.id}`);
    },
    hide(flat) {
      this.$modal.hide(`flat-preview:${flat.building.slug}-${flat.id}`);
    },
    updateSlidesPerView() {
      console.log('aaaaaaaaaaaaaaaaa')
      console.log('WIDTH: ', window.screen.width)
      // this.swiperOption.slidesPerView = window.screen.width < 640 ? 1  : 3

    }
  },
  computed: {
    // slidesPerView(){
    //   console.log("WIDTH: ", window.screen.width)
    //   return  window.screen.width < 640 ? 1  : 3
    // }
  },
  created() {
    // this.updateSlidesPerView()
    window.addEventListener('resize', this.updateSlidesPerView);
  },
  destroyed() {
    window.removeEventListener('resize', this.updateSlidesPerView);
  },
}
</script>

<style lang="scss" scoped>

.swiper {

  // .swiper-slide {
  //   background: #444;
  // }
  div.swiper-button-prev,
  div.swiper-button-next {

    color: #5ED2B8;
  }
}

<
/
style >