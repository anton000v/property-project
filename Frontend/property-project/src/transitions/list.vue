<template>
    <transition name="cards">
        <slot></slot>
    </transition >
</template>

<script>
export default {
    
}
</script>

<style scoped>

/* .cards-enter-active {
  transition: opacity 0.5s linear, transform 0.4s linear;
}
.cards-enter{
    transform: translateY(100vh);
    opacity: 0;
} */

.cards-enter-active {
  transition: opacity 0.5s linear, transform 0.3s linear;
}
.cards-enter{
    transform: translateY(20px);
    opacity: 50%;
}
.cards-leave-active {
    /* transform: translateY(-15px); */
    /* transition: opacity .2s linear */
    /* transition: opacity 0.05s linear, transform 0.3s linear; */
}
.cards-leave-to {
    /* transform: translateY(-5px); */
    /* opacity: 40%; */
    /* transform: translateY(-15px); */
    /* transform: translateY(-30px); */
    /* opacity: 50%; */
}
</style>