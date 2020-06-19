<template>
    <transition name="pages">
        <slot></slot>
    </transition>
</template>

<script>
export default {
    
}
</script>

<style scoped>

.pages-enter-active {
  transition: opacity 0.5s linear, transform 0.3s linear;
}
.pages-enter{
    transform: translateY(5px);
    /* opacity: 90%; */
}
.pages-leave-active {
    /* transform: translateY(-15px); */
    /* transition: opacity .2s linear */
}
.pages-leave-to {
    /* transform: translateY(-5px); */
    /* opacity: 40%; */
    /* transform: translateY(-15px); */
}

</style>