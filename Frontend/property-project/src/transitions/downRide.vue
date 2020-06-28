<template>
    <transition name="down-ride">
        <slot></slot>
    </transition>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.down-ride-enter-active, .down-ride-leave-active {
  transition:  .5s ease;
}
.down-ride-enter, .down-ride-leave-to /* .fade-leave-active до версии 2.1.8 */ {
    transform: translateY(-10px);
    opacity: 0;
}
</style>