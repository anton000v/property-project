<template>  
    <div class="main-wrapper">
        <div>
            <div class='min-h-screen'>
                <TransitionHeaderChange>
                    <vHeaderMain v-if="isMainHeaderActive" />
                    <vHeaderLittle v-else/>
                </TransitionHeaderChange>
                <TransitionPages>
                    <router-view :key="$route.name"/>
                </TransitionPages>
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
export default {
    components: {
        Footer,
        vHeaderMain,
        vHeaderLittle,
        TransitionHeaderChange,
        TransitionPages
    },
    watch:{
        $route: "updateHeader"
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
    },
    mounted() {
        this.updateHeader()
    },
    computed: {
      ...mapGetters([
        'isMainHeaderActive', 
        ]),
    },
}

</script>