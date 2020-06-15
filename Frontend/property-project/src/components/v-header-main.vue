<template>
  <div
      class="h-48 relative pt-16 pb-32 flex content-center items-center justify-center"
      style="min-height: 75vh;"
    >
      <div
        class="absolute top-0 w-full h-full bg-center bg-cover"
        :style="{ backgroundImage: 'url(' + require('@/assets/images/header.png') + ')' }">
      
        <span
          id="blackOverlay"
          class="w-full h-full absolute opacity-75 bg-black"
        ></span>
      </div>
      <div class="container relative mx-auto">
        <div class="items-center flex flex-wrap">
          <div class="w-full lg:w-6/12 px-4 ml-auto mr-auto text-center">
            <div class="pr-12">
              <h1 class="text-white font-semibold text-5xl">
                property - project
              </h1>
              <p class="mt-4 text-lg text-gray-300">
                Поиск новостроев
              </p>
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

export default{
  // props: ['Header'],
  data(){
    return {
      // djangoImagesPathInComponentsFolder:djangoImagesPathInComponentsFolder,
      // testPath:"../../../../Backend/PropertyProject_engine/PropertyProject_api/media/126403.jpg",
    }
  },
}
</script>
