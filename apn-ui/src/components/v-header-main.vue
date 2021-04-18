<template>
  <div
      class="relative pt-16 pb-32 flex content-center items-center justify-center"
      style="min-height: 60vh;"
  >
    <div class="absolute top-0 w-full h-full bg-center bg-cover bg-myPageBackground md:bg-white"
    >
      <div
          ref="mainHeader"
          class="absolute w-full h-full bg-cover"
          :style="{ backgroundImage: 'url(' + require('@/assets/images/header-background.png') + ')'  }"></div>

      <span
          id="blackOverlay"
          class="w-full h-full absolute opacity-75 bg-black"
      ></span>
    </div>
    <div class="container relative mx-auto ">
      <div class="items-center flex flex-wrap">
        <div class="px-4 m-auto">
          <div class="text-center">
            <v-logo></v-logo>
          </div>
        </div>
      </div>
    </div>
    <div
        class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden"
        style="height: 70px; transform: translateZ(0px);"
    >
      <svg
          class="absolute bottom-0 overflow-hidden"
          xmlns="http://www.w3.org/2000/svg"
          preserveAspectRatio="none"
          version="1.1"
          viewBox="0 0 2560 100"
          x="0"
          y="0"
      >
        <polygon
            class="text-myPageBackground fill-current"
            points="2560 0 2560 100 0 100"
        ></polygon>
      </svg>
    </div>
  </div>


</template>

<script>
// import { KinesisContainer, KinesisElement} from 'vue-kinesis'
import {TimelineMax, Linear} from 'gsap'
import vLogo from './v-logo';

export default {
  // props: ['Header'],
  data() {
    return {
      tween: new TimelineMax({repeat: -1})
    }
  },
  mounted() {
    // Based on https://greensock.com/forums/topic/17160-moving-background/
    this.tween
        .to(this.$refs.mainHeader, 60, {
          backgroundPosition: "-2935px 0px",
          ease: Linear.easeNone
        })
  },
  components: {
    vLogo
  },
  methods: {}
}
</script>

