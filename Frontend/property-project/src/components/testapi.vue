<template>

<div>
  <h2>Micro districts choices </h2>
  <p>{{ microDistrictsChoices }} </p>
  <h2>buildings</h2>
  <p>{{ allBuildingsList }}</p>
</div>
</template>

<script>
// import axios from 'axios'

export default{
  props: ['Testapi'],
  data() {
    return {
      microDistrictsChoices: null,
      allBuildingsList: null,
    };
  },
  mounted() {
    const axios = require('axios');

      axios.get('http://127.0.0.1:8000/api/get-micro-districts/').then(resp => {
          this.microDistrictsChoices = resp.data;
      });
      axios.get('http://127.0.0.1:8000/api/find-buildings/').then(resp => {
          this.allBuildingsList = resp.data;
      })

    // axios
    //   .get('http://127.0.0.1:8000/api/get-micro-districts/')
    //   .then(response => (this.info = response.data));
  }
}

</script>
