<template>
  <div
      class="h-96 relative pt-16 pb-32 flex content-center items-center justify-center"
      style="min-height: 60vh;"
    >
      <div
        class="absolute top-0 w-full h-full bg-center bg-cover bg-myPageBackground md:bg-white"
        :style="{ backgroundImage: 'url(' + require('@/assets/images/header-apn-1.png') + ')' }">
        
      
        <span
          id="blackOverlay"
          class="w-full h-full absolute opacity-75 bg-black"
        ></span>
      </div>
      <div class="container relative mx-auto ">
        <div class="items-center flex flex-wrap">
          <div class="px-4 ml-auto mr-auto">
            <div>
              <!-- <div class=" bg-gray-400"> -->
<!--                <h1 class="pt-6 text-white font-semibold text-4xl md:text-5xl text-center">-->
<!--                  <span class="bg-myPageBackground border rounded-l-lg p-4 text-myHeaderColor">Ок.</span><span class="p-4 text-myPageBackground border rounded-r-lg">Найдем</span>-->
<!--                  &lt;!&ndash; <img :src="require('@/assets/images/logo1.svg')" class="m-auto"> &ndash;&gt;-->
<!--                </h1>-->
              <hi class="font-furore text-white text-6xl">
                Автостопом<br>По<br>Новостроям
              </hi>
              <!-- </div> -->
              <p class="mt-4 text-lg text-myPageBackground text-center">
                Наверное лучший поиск новостроев Харькова
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
      // testPath:"../../../../Backend/PropertyProject_engine/api/media/126403.jpg",
    }
  },
}
</script>
