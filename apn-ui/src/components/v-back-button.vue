<template>
    <div>
        <div v-if="canBack" class="relative rounded-lg flex md:hover:shadow-lg  text-myMint-100 md:hover:text-white cursor-pointer" @click="$router.go(-1)">
            <div class="w-full pt-4 inline-flex items-center md:transition md:duration-500 md:ease-in-out  md:transform md:hover:-translate-x-10">
                <!-- <div class=""> -->
                    <KeyboardBackspaceIcon  :size="40"/>
                <!-- </div> -->
                <span class="pl-5 text-sm md:text-xl">{{ canBackText }}</span>
            </div>
        </div>
        <div v-else class="relative rounded-lg flex md:hover:shadow-lg  text-myMint-100 md:hover:text-white cursor-pointer" @click="$router.push(noBackUrl)">
            <div class="w-full pt-4 inline-flex items-center md:transition md:duration-500 md:ease-in-out  md:transform md:hover:-translate-x-10">
                <!-- <div class=""> -->
                    <KeyboardBackspaceIcon  :size="40"/>
                <!-- </div> -->
                <span class="pl-5 text-sm md:text-xl">{{ canNotBackText }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import KeyboardBackspaceIcon from 'vue-material-design-icons/KeyboardBackspace'
export default {
    props:{
        canBackText:{
            type:String,
            default: 'Назад'
        },
        canNotBackText:{
            type:String,
            default: 'На главную'
        },
        noBackUrl:{
            type:String,
            default: '/'
        }
    },
    data(){
        return{
            prevRoute: null,
        }
    },
    components:{
        KeyboardBackspaceIcon
    },
    computed:{
        canBack(){
            if(window.history.length > 1){
                return true
            }
            return false
        },
        // noBackUrl(){
        //     return this.$route.
        // }
    },
    // beforeRouteEnter(to, from, next) {
    //     alert()
    //     next(vm => {
    //         alert()
    //         vm.prevRoute = from
    //         // console.log('FFFFFFFf')
    //         // console.log(from)
    //         // console.log(vm.$route)
    //         // console.log(vm.$router)
    //         // alert(vm.prevRoute.path)
    //     })
    // },
}
</script>