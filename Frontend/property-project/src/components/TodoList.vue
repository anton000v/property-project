<template>

  <ul>
    <li v-for="(todo, index) in todoList" @click="deleteTodo(index)" :key="index">{{ todo }}</li>
  </ul>

</template>

<script>
export default{
  props: ['todoList'],
  methods: {
    deleteTodo(index){
      this.$emit('delete-todo', index);
    }
  }
}
</script>
