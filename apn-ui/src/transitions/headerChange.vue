<template>
    <transition name="header-change" mode="out-in">
        <slot></slot>
    </transition>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.header-change-enter-active {
  transition: opacity .7s linear, transform 0.3s linear;
}
.header-change-enter{
    transform: translateY(-5px);
    /* opacity: 0% */
}
.header-change-leave-active {
    /* transform: translateY(-2px); */
    /* transition: opacity .2s linear; */
}
.header-change-leave-to {
    /* transform: translateY(-5px); */
    /* opacity: 40%; */
    /* transform: translateY(5px); */
    /* transform: translateY(-15px); */
}

</style>