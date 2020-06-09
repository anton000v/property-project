


<template>
<!-- <div :class="'swiper-container '+field_name" > -->
  
  <swiper :id="'swiper-'+uniqueStr" :class="'swiper '+uniqueStr" :options="swiperOption">
   
        <swiper-slide 
      v-for="image in images"
      :key="image.id"
      >
    <div class="swiper-zoom-container">
      <img :src="image[field_name]">
    </div>
    </swiper-slide>
    <div :class="'swiper-pagination-'+uniqueStr" slot="pagination"></div>
    <div  :class="'button-prev-'+uniqueStr" slot="button-prev"></div>
    <div  :class="'button-next-'+uniqueStr" slot="button-next"></div>
  </swiper>
  <!-- </div> -->
</template>

<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'

  export default {
    // name: this.uniqueStr,
    title: 'Progress pagination',
    props:{
      images:{
        type:Array
      },
      field_name:{
        type:String
      },
      slug:{
        type:String
      }

    },
    components: {
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        uniqueStr:this.slug+'-'+this.field_name,
        swiperOption: {
          pagination: {
            el: '.swiper-pagination '+this.uniqueStr,
            type: 'progressbar'
          },
          navigation: {
            // nextEl: '#button-next-'+this.uniqueStr,
            // prevEl: '#button-prev-'+this.uniqueStr,
              nextEl: '.button-next-'+this.uniqueStr,
              prevEl: '.button-prev-'+this.uniqueStr,
          }
        }
      }
    }
  }
</script>


