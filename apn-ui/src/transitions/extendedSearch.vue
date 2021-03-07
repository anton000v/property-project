<template>
    
    <transition name="extended-search">
        <slot></slot>
    </transition>

</template>

<script>
export default {
    
}
</script>

<style scoped>

.extended-search-enter-active {
  transition: opacity 0.3s linear, transform 1s linear;
}
.extended-search-enter{
    /* transform: translateX(100vh); */
    opacity: 0%
}
.extended-search-leave-active {
    /* transform: translateY(-2px); */
    transition: opacity 0.3s linear
}
.extended-search-leave-to {
    /* transform: translateY(100vh); */
    opacity: 0%;
    /* transform: translateY(5px); */
    /* transform: translateY(-15px); */
}

</style>