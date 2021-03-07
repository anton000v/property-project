<template>
    <div>
        <!-- {{ currentOffset }}
        ||
        {{ fullWindowHeight }}
        || -->
        <!-- {{ showBackToTopButton }} -->
        <FromDownScreenTransition>
            <div v-if="showBackToTopButton" @click="backToUp" class="fixed bottom-0 right-0 m-1 lg:m-20 cursor-pointer md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out">
                <div class="hidden md:block">
                    <ArrowUpCircleIcon class="text-myHeaderColor md:hover:bg-myHeaderColor md:hover:text-myMint-400" :size="55" title="Вверх" />
                </div>
                <div class="block md:hidden">
                    <ArrowUpCircleIcon class="text-myHeaderColor md:hover:bg-myHeaderColor md:hover:text-myMint-400" :size="40" title="Вверх" />
                </div>
            </div>
        </FromDownScreenTransition>
    </div>
</template>

<script>
// import { ArrowUpCircleIcon } from 'vue-material-design-icons/A'
import ArrowUpCircleIcon from 'vue-material-design-icons/ArrowUpCircle';
import FromDownScreenTransition from '../transitions/fromDownScreen'


export default {
    components:{
        ArrowUpCircleIcon,
        FromDownScreenTransition,

    },
    props: {
        currentOffset: Number,
        fullWindowHeight: Number
    },
    data(){
        return{
            // showBackToTopButton: false,
            // fullHeightSize: 0,
        }
    },
    computed:{
        showBackToTopButton(){
            if(this.currentOffset > this.fullWindowHeight/2){
                return true
            }
            return false
        }
    },
    methods: {
        backToUp(){
            var VueScrollTo = require('vue-scrollto');
            var options = {
                easing: 'ease-in-out',
                force: true,
                cancelable: true,
                x: false,
                y: true
            }
            VueScrollTo.scrollTo('#top', 500, options)
        }
    }
    // watch(){

    // }
    // created () {
    //     //  window.addEventListener('scroll', this.handleScroll);
    //      window.addEventListener('resize', this.updateAnchorsOffset);
    // },
    // destroyed () {
    //     // window.removeEventListener('scroll', this.handleScroll);
    //     window.removeEventListener('resize', this.updateAnchorsOffset);
    // },
    // handleResize () {
    //     this.fullHeightSize = window.innerHeight
    //     alert(this.fullHeightSize)
    //     // alert()
    //     // if (window.pageYOffset > this.window.innerHeight) {
    //     //     this.showBackToTopButton = true
    //     //     // this.anchorsInfo.element.classList.add("text-center");

    //     // } else {
    //     //     this.showBackToTopButton = false
    //     //     // this.anchorsInfo.element.classList.remove("text-center");
    //     // }
    // },
}
</script>
