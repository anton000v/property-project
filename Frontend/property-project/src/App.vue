<template>
  <div id="app">
    <!-- <b-container fluid> -->

      <Header/>
      <Body/>
      
    <!-- </b-container> -->
  </div>
</template>

<script>

import Header from './components/header.vue';
import Body from './components/body.vue';

export default {
  name: 'App',
  components: {
    Header,
    Body,
  },

}
</script>

<style>

</style>
