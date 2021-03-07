<template>
    <transition name="slow-appearance">
        <slot></slot>
    </transition>
</template>

<script>
export default {
    
}
</script>

<style scoped>

.slow-appearance-enter-active, .slow-appearance-leave-active {
  transition: opacity .5s;
}
.slow-appearance-enter, .slow-appearance-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}

</style>