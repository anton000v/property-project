<template>
  <div id="app">

      <Header/>
      <!-- <Body/> -->
      <BuildingsSearchKit/>
      <BuildingsList/>
  </div>
</template>

<script>

import Header from './components/header.vue';
// import Body from './components/body.vue';
import BuildingsList from './components/buildingsList'
import BuildingsSearchKit from './components/buildingsSearchKit'
export default {
  name: 'App',
  components: {
    Header,
    // Body,
    BuildingsList,
    BuildingsSearchKit,
  },

}
</script>

<style>

</style>
