<template>
  <div id="app">
    <b-container fluid>
    <Header/>
    <Body/>
    </b-container>
  </div>
</template>

<script>

import Header from './components/header.vue';
import Body from './components/body.vue';
export default {
  name: 'App',
  // data(){
  //   return {
  //     todos: ['Ремонт', 'Something else', 'lalala']
  //   }
  // },
  components: {
    // TodoList,
    Header,
    Body,
  },
  // methods: {
  //   deleteTodo(index){
  //     this.todos.splice(index, 1);
  //   }
  // }
}
</script>

<style>

</style>
