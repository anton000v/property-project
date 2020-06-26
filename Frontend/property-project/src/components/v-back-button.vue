<template>
    <div>
        <div v-if="canBack" class="relative rounded-lg flex md:hover:shadow-lg  text-myMint-100 md:hover:text-white cursor-pointer" @click="$router.go(-1)">
            <div class="w-full pt-4 inline-flex items-center transition duration-500 ease-in-out  transform hover:-translate-x-10">
                <!-- <div class=""> -->
                    <KeyboardBackspaceIcon  :size="40"/>
                <!-- </div> -->
                <span class="pl-5 text-sm md:text-xl">{{ canBackText }}</span>
            </div>
        </div>
        <div v-else class="relative rounded-lg flex md:hover:shadow-lg  text-myMint-100 md:hover:text-white cursor-pointer" @click="$router.push(prevRoute.fullPath)">
            <div class="w-full pt-4 inline-flex items-center transition duration-500 ease-in-out  transform hover:-translate-x-10">
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
            default: 'Назад'
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
    }
}
</script>