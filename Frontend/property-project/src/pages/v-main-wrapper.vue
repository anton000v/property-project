<template>  
    <div class="main-wrapper">
        <div>
        <!-- <vue-page-transition name="overlay-left-right"> -->
            <!-- <md-transition> -->
                <div class='min-h-screen'>
                    <vHeaderMain v-if="isMainHeaderActive" />
                    <vHeaderLittle v-else/>
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
import vHeaderMain from '../components/v-header-main'
import vHeaderLittle from '../components/v-header-little'
import {mapGetters ,mapMutations } from 'vuex'
// import TransitionPage from '../transitions/v-transition-page';
export default {
    components: {
        Footer,
        vHeaderMain,
        vHeaderLittle,
    },
    // data(){
    //     return{
    //         isMainHeader: true 
    //     }
    // },
    watch:{
        $route: "updateHeader"
    },
    methods: {
        ...mapMutations([
            'changeMainHeader',
        ]),
        updateHeader(path){
            // alert(path.path)
            if(path.path == '/'){
                if(!this.isMainHeaderActive){
                    this.changeMainHeader(true)
                }
            }
            else{
                // alert("dasdfsdf")
                this.changeMainHeader(false)
            }
        }
    },
    computed: {
      ...mapGetters([
        'isMainHeaderActive', 
        ]),
    },
}

</script>