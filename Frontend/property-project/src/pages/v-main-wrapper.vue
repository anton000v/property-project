<template>  
    <div class="main-wrapper">
        <div>
            <div class='min-h-screen'>
                <!-- {{ isLoaded }} -->
                <vHeaderMain v-if="isMainHeaderActive" />
                <vHeaderLittle v-else/>
                <router-view/>
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
export default {
    components: {
        Footer,
        vHeaderMain,
        vHeaderLittle,
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
        
        // updateInfo(path){
        //     updateHeader(path)

        // }
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