<template>
  <div id="app" class="bg-myPageBackground">
      <vMainWrapper/>
  </div>
</template>

<script>
import vMainWrapper from './pages/v-main-wrapper'

export default {
  name: 'App',
  components: {
    vMainWrapper,
  },
}
</script>

<style>

/* body{
  background-color:black;
} */

body {
  /* background: -webkit-gradient(linear, left top, left bottom, from(#fff), to(#5ED2B8)) fixed; */
}

</style>