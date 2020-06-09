<template>  
    <div class="main-wrapper">
        <div class="bg-gray-300">
        <!-- <vue-page-transition name="overlay-left-right"> -->
            <md-transition>
                <router-view/>
            </md-transition>
            </div>
        <!-- </vue-page-transition> -->
    </div>
</template>

<script>


// import TransitionPage from '../transitions/v-transition-page';
export default {
    // components: {
    //     TransitionPage,
    // },
}

</script>