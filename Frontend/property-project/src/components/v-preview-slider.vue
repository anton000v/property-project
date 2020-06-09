
<template>
  <swiper class="swiper h-full" :options="swiperOption">
    <!-- <swiper-slide>
      <div class="swiper-zoom-container">
        <img src="/images/example/4.jpg">
      </div>
    </swiper-slide> -->
    <swiper-slide 
      v-for="image in images"
      :key="image"
      >
          <div class="swiper-zoom-container">
        <img :src="image">
      </div>
    </swiper-slide>

    <!-- <swiper-slide>
      <div class="swiper-zoom-container">
        <img src="/images/example/8.jpg">
      </div>
    </swiper-slide> -->
    <div class="swiper-pagination swiper-pagination-white" slot="pagination"></div>
    <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div>
  </swiper>
</template>




<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'
  export default {
    // name: this.uniqueStr,
    // title: 'Progress pagination',
    title: 'Zoom',
    props:{
      images:{
        type:Array
      },
      slug:{
        type:String
      },
      height:{
          type:Number
      }
    },
    components: {
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        swiperOption: {
          zoom: true,
          pagination: {
            el: '.swiper-pagination'
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
         }
        }
    },
    computed: {
        swiperCss() {
            return {
                '--height': this.height + 'px',
                // '--height': this.height + 'px'
            }
        }
    }

  }
</script>

<style lang="scss" scoped>


  .swiper {
      
    .swiper-slide {
      background: #444;
    }
  }
</style>