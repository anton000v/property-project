<template>
    <transition name="from-down">
        <slot></slot>
    </transition>
</template>

<script>
export default {
    
}
</script>

<style scoped>

.from-down-enter-active {
  transition: opacity 1.1s linear, transform 1s linear;
}
.from-down-enter{
    transform: translateX(100vh);
    opacity: 0%
}
.from-down-leave-active {
    /* transform: translateY(-2px); */
    transition: opacity 1.1s linear, transform 1s linear;
}
.from-down-leave-to {
    transform: translateY(100vh);
    opacity: 0%;
    /* transform: translateY(5px); */
    /* transform: translateY(-15px); */
}

</style>