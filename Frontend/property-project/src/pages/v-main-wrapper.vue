<template>  
    <div id="top" class="main-wrapper">
        <div>
            <div class='min-h-screen'>
                <!-- <div class="fixed top-0 bg-white w-full z-50">
                {{ currentWindowOffset }} {{ TransitionPages }}
                </div> -->
                <TransitionHeaderChange>
                    <vHeaderMain v-if="isMainHeaderActive" />
                    <vHeaderLittle v-else/>
                </TransitionHeaderChange>
                <TransitionPages>
                    <router-view :key="$route.name"/>
                </TransitionPages>
                <div class='z-50'>
                    <vBackToTopButton :currentOffset="currentWindowOffset" :fullWindowHeight="fullWindowHeight"/>
                </div>
            </div>
            <Footer/>
        </div>
    </div>
</template>

<script>

import Footer from '../components/v-footer'
import vHeaderMain from '../components/v-header-main'
import vHeaderLittle from '../components/v-header-little'
import {mapGetters ,mapMutations } from 'vuex'
import TransitionHeaderChange from '../transitions/headerChange'
import TransitionPages from '../transitions/pages'
import vBackToTopButton from '../components/v-back-to-top'
export default {
    components: {
        Footer,
        vHeaderMain,
        vHeaderLittle,
        TransitionHeaderChange,
        TransitionPages,
        vBackToTopButton
    },
    watch:{
        $route: "updateHeader"
    },
    data(){
        return {
            currentWindowOffset: window.pageYOffset,
            fullWindowHeight:window.innerHeight ,
        }
    },
    methods: {
        ...mapMutations([
            'changeMainHeader',
        ]),
        updateHeader(){
            if(this.$route.path == '/'){
                if(!this.isMainHeaderActive){
                    this.changeMainHeader(true)
                }
            }
            else{
                this.changeMainHeader(false)
            }
        },
        updateWindowOffset() {
            this.currentWindowOffset = window.pageYOffset
        },
        updatefullWindowWidth(){
            this.fullWindowHeight = window.innerHeight
        },
    },
    mounted() {
        this.updateHeader()
    },
    computed: {
      ...mapGetters([
        'isMainHeaderActive', 
        ]),
    },
    created () {
         window.addEventListener('scroll', this.updateWindowOffset);
         window.addEventListener('resize', this.updatefullWindowWidth);
            // this.anchorsOffsetTop = this.$refs.anchors.$el.offsetTop;
            // alert(this.anchorsOffsetTop)

    },
    destroyed () {
        window.removeEventListener('scroll', this.updateWindowOffset);
        window.removeEventListener('resize', this.updatefullWindowWidth);
    },

}

</script>