<template>
  <div>
    <h1 class="font-furore text-white text-center" :class="hTextStyles">
      Автостопом<br>По<br>Новостроям
    </h1>
    <p class="mt-4 text-lg text-myPageBackground text-center">
      Наверное лучший поиск новостроев Харькова
    </p>
  </div>
</template>

<script>
export default {
  name: "v-logo",
  props: {
    hTextStyles: {
      type: Array,
      default: () => {
        return ['text-4xl', 'md:text-6xl']
      }
    },
  }
}
</script>

<style scoped>

</style>