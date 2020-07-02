<template>
    <div class="cursor-default " @mouseover="socialMouseHover=true" @mouseleave="socialMouseHover = false">     
                            <div class="rounded-lg px-4 py-2">
                               <div class="inline-flex items-center">
                                <ShareVariantIcon :size="20" class="transition duration-500 text-myHeaderColor" :class="{'text-myMint-400':socialMouseHover}"/>
                                    <p class="pl-2 text-md">Поделиться</p>
                               </div>
                            </div>
                            <div v-show="socialMouseHover" class="absolute z-50 p-2 right-0 rounded-lg bg-myHeaderColor">
                                <div class="flex">
                                    <ViberButton 
                                        :description="'Oк. Найдем! ' + descriptionText" 
                                        :url="pageUrl" 
                                        v-bind:isBlank="false" 
                                        class="share-button--circle"
                                        btnText
                                    />
                                    <TelegramButton 
                                        :description="'Oк. Найдем! ' + descriptionText" 
                                        :url="pageUrl" 
                                        v-bind:isBlank="false" 
                                        class="share-button--circle"
                                        btnText
                                    />
                                    <VkontakteButton 
                                        :description="'Oк. Найдем! ' + descriptionText" 
                                        :url="pageUrl" 
                                        v-bind:isBlank="false" 
                                        class="share-button--circle" 
                                        btnText
                                    />
                                </div>

                                <span @click="copyAddress" class="w-full text-sm pt-2 text-white cursor-pointer">Скопировать ссылку</span>
                                <input ref="pageUrl" type="hidden" :value="pageUrl">
                                <div v-show="addressCopiedSuccessfully" class="text-center">
                                    <span class="text-myMint-400 text-sm ">Скопировано!</span>
                                </div>
                                <div v-show="addressCopiedUnsuccessfully" class="text-center">
                                    <span class="text-myMint-400 text-sm text-center">Возникла ошибка</span>
                                </div>
                            </div>
                        </div>
</template>

<script>
import TelegramButton from "vue-share-buttons/src/components/TelegramButton";
import ViberButton from "vue-share-buttons/src/components/ViberButton";
import VkontakteButton from "vue-share-buttons/src/components/VkontakteButton";
import ShareVariantIcon from 'vue-material-design-icons/ShareVariant'

export default {
    props:{
        pageUrl:{
            type:String,
            default:null,
        },
        descriptionText:{
            type: String,
            default: null
        }
    },
    components:{
        TelegramButton,
        ViberButton,
        VkontakteButton,
        ShareVariantIcon,
    },
    data(){
        return{
            socialMouseHover: false,
            addressCopiedSuccessfully: false,
            addressCopiedUnsuccessfully:false,
        }
    },
    computed: {
        // pageUrl: function(){ 
        //     let url = this.$router.resolve({ 
        //         name: 'flat-page',
        //         params: { slug:this.flat.building.slug, id:this.flat.id },
        //     }).href
        //     return window.location.origin + "/" + url
        // },
        // fullFlatAddress: function(){
        //     let house_letter = this.flat.building.house_letter != null ? this.flat.building.house_letter : ''
        //     // alert(house_letter)
        //     // console.log(house_letter)
        //     return this.flat.building.street + ' ' + this.flat.building.house_number + house_letter
        // }
    },
    methods: {
        copyAddress () {
            let testingCodeToCopy = this.$refs.pageUrl
            testingCodeToCopy.setAttribute('type', 'text')    // 不是 hidden 才能複製
            testingCodeToCopy.select()
            // alert(testingCodeToCopy)
            try {
                // document.execCommand('copy');
                var successful = document.execCommand('copy');
                if(successful){
                    this.addressCopiedSuccessfully = true
                    setTimeout(()=>{
                        this.addressCopiedSuccessfully = false
                    }, 
                    1000);
                    // alert()
                }
                if(!successful){
                    this.addressCopiedUnsuccessfully = true
                    setTimeout(()=>{
                        this.addressCopiedUnsuccessfully = false
                    }, 
                    1000);
                }
                // var msg = successful ? 'successful' : 'unsuccessful';
                // alert('Testing code was copied ' + msg);
            } catch (err) {
                // alert('Oops, unable to copy');
            }

            /* unselect the range */
            testingCodeToCopy.setAttribute('type', 'hidden')
            window.getSelection().removeAllRanges()
            },
    },
}
</script>