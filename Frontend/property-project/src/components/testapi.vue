<template>

<p> {{ info }} </p>

</template>

<script>
// import axios from 'axios'

export default{
  props: ['Testapi'],
  data() {
    return {
      info: null
    };
  },
  mounted() {
    const axios = require('axios');

      axios.get('http://127.0.0.1:8000/api/get-micro-districts').then(resp => {

          console.log(resp.data);
      });

    // axios
    //   .get('http://127.0.0.1:8000/api/get-micro-districts/')
    //   .then(response => (this.info = response.data));
  }
}

</script>
