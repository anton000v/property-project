<template>
  <div>
    <TodoList v-bind:todo-list="todos" @delete-todo="deleteTodo"/>
    <br>
    <Testapi/>
  </div>
</template>

<script>
import TodoList from './TodoList.vue';
import Testapi from './testapi.vue';

export default{
  props: ['Body'],
  data(){
    return {
      todos: ['Ремонт', 'Something else', 'lalala']
    }
  },
  components: {
    TodoList,
    Testapi
  },
  methods: {
    deleteTodo(index){
      this.todos.splice(index, 1);
    }
  }
}
</script>
