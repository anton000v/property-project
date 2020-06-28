<template>
  <div
      class="h-14 md:h-30 bg-myHeaderColor relative pt-16 pb-32 flex content-center items-center justify-center"
      style="min-height: 30vh;"
    >
      <div
        class="absolute top-0 w-full h-full bg-center bg-cover "
        >
      

      </div>
      <div class="container relative mx-auto">
        <div class="items-center flex flex-wrap">
          <div class="w-full xl:w-6/12 px-4 ml-auto mr-auto text-center">
            <!-- <div class=""> -->
              <router-link to="/">
                <h1 class="text-white font-semibold text-2xl md:text-5xl lg:text-5xl">
                    <!-- property - project -->
                    <span class="bg-myPageBackground border rounded-l-lg p-4 text-myHeaderColor">Ок.</span><span class="p-4 text-myPageBackground border rounded-r-lg">Найдем</span>
                </h1>
              </router-link>
              <p class="mt-4 text-lg text-myPageBackground text-center">
                Поиск новостроев Харькова. 
              </p>
            <!-- </div> -->
          </div>
        </div>
      </div>
      <!-- <div
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
      </div> -->
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
