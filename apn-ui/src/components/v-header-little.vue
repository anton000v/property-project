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
          <router-link to="/">
          <v-logo :h-text-styles="['text-2xl', 'md:text-4xl']"></v-logo>
          </router-link>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import vLogo from './v-logo';

export default {
  components: {
    vLogo
  },
  data() {
    return {
    }
  },
}
</script>
