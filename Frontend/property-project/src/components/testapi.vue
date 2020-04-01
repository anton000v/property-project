<template>

<div>
  <h2>Buildings JSON</h2>
  <p> {{ buildings }} </p>

  <h2>Micro districts choices </h2>
  <p>{{ microDistrictsChoices }} </p>
</div>
</template>

<script>
// import axios from 'axios'

export default{
  props: ['Testapi'],
  data() {
    return {
      buildings: null,
      microDistrictsChoices: null,
    };
  },
  mounted() {
    const axios = require('axios');

      axios.get('http://127.0.0.1:8000/api/buildings/').then(resp => {
          this.buildings = resp.data;
      });
      axios.get('http://127.0.0.1:8000/api/get-micro-districts/').then(resp => {
          this.microDistrictsChoices = resp.data;
      });

    // axios
    //   .get('http://127.0.0.1:8000/api/get-micro-districts/')
    //   .then(response => (this.info = response.data));
  }
}

</script>
