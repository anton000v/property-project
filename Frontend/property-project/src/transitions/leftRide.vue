<template>
    <transition name="left-ride">
        <slot></slot>
    </transition>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.left-ride-enter-active, .left-ride-leave-active {
  transition:  .5s ease;
}
.left-ride-enter, .left-ride-leave-to /* .fade-leave-active до версии 2.1.8 */ {
    transform: translateX(-10px);
    opacity: 0;
}
</style>