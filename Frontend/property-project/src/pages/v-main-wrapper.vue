<template>  
    <div class="main-wrapper">
        <div>
        <!-- <vue-page-transition name="overlay-left-right"> -->
            <!-- <md-transition> -->
                <div class='min-h-screen'>
                    <router-view/>
                </div>
                <Footer/>
            <!-- </md-transition> -->
        </div>
        <!-- </vue-page-transition> -->
    </div>
</template>

<script>


import Footer from '../components/v-footer'
// import TransitionPage from '../transitions/v-transition-page';
export default {
    components: {
        Footer,
    },
}

</script>