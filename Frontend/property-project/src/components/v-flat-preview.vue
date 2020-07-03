<template>
    <modal 
    :name="'flat-preview:'+`${flat.building.slug}-${flat.id}`"
    :width="modalWidth"
    :height="modalHeight"
    :adaptive="true"
    :scrollable="true"
    
    >

        <div class="bg-myPageBackground">
            <div class="items-center text-center w-full">
                <div class="grid md:grid-cols-2 justify-center">
                    <div class="flex h-16">
                        <p class="m-auto text-2xl font-bold">{{fullFlatAddress}}</p>
                    </div>
                    <router-link :to="{name:'flat-page', params:{slug:flat.building.slug,id:flat.id}}">
                        <div class="flex h-16 bg-myHeaderColor text-white hover:bg-myMint-400 transition duration-500 ease-in-out hover:rounded-none hover:opacity-40 transform hover:translate-y-1 hover:shadow-2xl overflow-hidden shadow-md">  
                            <p class="m-auto text-xl"> Открыть полностью </p>
                        </div>
                    </router-link>
                </div>
            </div>
            <div id='preview-slider' class='py-2 h-screen/2' v-if="sliderImages.length">
                <vPreviewSlider 
                :images="sliderImages" 
                />
            </div>
            <div id='preview-slider' class='py-2 h-screen/2' v-else>
                <vPreviewSlider 
                    :images="[require('@/assets/images/no-photo-yet.jpg')]" 
                />
            </div>
            <div class="pr-5 pl-5 pb-5"> 
                <div class= 'w-full'>
                    <div class="flex justify-between m-2 relative">
                        <div class="border rounded-lg border-myMint-400 text-gray-700 text-xl px-4 py-2">
                            {{ flat.price }}$
                            
                        </div>
                        <vShareDropdown :pageUrl="pageUrl" :descriptionText="`${fullFlatAddress}. Описание: ${flat.description}.`"/>
                    </div>
                    <div class="flex justify-center justify-center text-center justify-center gap-2">
                        <div v-if="flat.building.administrative_district != null" class="flex-1 rounded-lg flex-col shadow-sm transition duration-500 hover:shadow-md">
                            <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                <div class="inline-flex items-center">
                                    <HomeCityIcon class="text-myMint-400" :size="30"  />
                                    <div class="block xl:hidden flex-1 px-1  ">
                                        Админ. район
                                    </div>
                                    <div class="hidden xl:block flex-1 px-2  ">
                                        Административный район
                                    </div>
                                </div>
                            </div>
                            <div class="rounded-lg bg-gray-200  text-gray-700 text-base md:text-lg text-center md:px-4 py-2 m-2">{{ flat.building.administrative_district }}</div>
                        </div>
                        <div v-if="flat.building.district != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                            <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                <div class="inline-flex items-center">
                                    <HomeGroupIcon class="text-myMint-400" :size="30" />
                                    <div class="flex-1 sm:px-1 px-2">
                                        Район
                                    </div>
                                </div>
                            </div>
                            <div class="rounded-lg bg-gray-200 text-gray-700 text-base md:text-lg text-center md:px-4 py-2 m-2">{{ flat.building.district }}</div>
                        </div>
                        <div v-if="flat.building.micro_district !== 'Не делится на микрорайоны'" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                            <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                <div class="inline-flex items-center">
                                    <DomainIcon class="text-myMint-400" :size="30" />
                                    <div class="flex-1 sm:px-1 px-2">
                                        Микрорайон
                                    </div>
                                </div>
                            </div>
                            <div class="bg-gray-200 rounded-lg text-gray-700 text-base md:text-lg  text-center md:px-4 py-2 m-1 md:m-2">{{ flat.building.micro_district }}</div>
                        </div>
                        <div v-if="flat.building.developer != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                            <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                <div class="inline-flex items-center">
                                    <HouseEditIcon class="text-myMint-400" :size="30" />
                                    <div class="flex-1 sm:px-1 px-2">
                                        Застройщик
                                    </div>
                                </div>
                            </div>
                            <div class="bg-gray-200 rounded-lg text-gray-700 text-base md:text-lg text-center  md:px-4 py-2 m-2">{{ flat.building.developer }}</div>
                        </div>
                    </div>
                
                    <div class="flex justify-center justify-center text-center justify-center gap-2">
                        <div v-if="flat.rooms != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                            <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                <div class="inline-flex items-center">
                                    <DoorIcon class="text-myMint-400" :size="30" />
                                    <div class="flex-1 sm:px-1 px-2">
                                        Комнат
                                    </div>
                                </div>
                            </div>
                            <div class="bg-gray-200 rounded-lg text-gray-700 text-base md:text-lg text-center  md:px-4 py-2 m-2">{{ flat.rooms }}</div>
                        </div>
                        <div v-if="flat.floor != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                            <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                <div class="inline-flex items-center">
                                    <HomeFloor0Icon class="text-myMint-400" :size="30" />
                                    <div class="flex-1 sm:px-1 px-2">
                                        Этаж / этажность:
                                    </div>
                                </div>
                            </div>
                            <div class="bg-gray-200 rounded-lg text-gray-700 text-base md:text-lg text-center  md:px-4 py-2 m-2">{{ flat.floor }}/{{ flat.building.number_of_storeys }}</div>
                        </div>
                        <div v-if="flat.living_area != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                            <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                <div class="inline-flex items-center">
                                    <RulerIcon class="text-myMint-400" :size="30" />
                                    <div class="flex-1 sm:px-1 px-2">
                                        S общ/жил/кух:  
                                    </div>
                                </div>
                            </div>
                            <div v-if="flat.kitchen_area" class="bg-gray-200 rounded-lg text-gray-700 text-base md:text-lg text-center  md:px-4 py-2 m-2">{{ flat.living_area + flat.kitchen_area }}/{{ flat.living_area }}/{{ flat.kitchen_area }} м<sup>2</sup></div>
                            <div v-else class="bg-gray-200 rounded-lg text-gray-700 text-base md:text-lg text-center  md:px-4 py-2 m-2">{{ flat.living_area }}/{{ flat.living_area }}/- м<sup>2</sup></div>
                        </div>
                        <div v-if="flat.price != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                            <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                <div class="inline-flex items-center">
                                    <CashUsdOutlineIcon class="text-myMint-400" :size="30" />
                                    <div class="flex-1 sm:px-1 px-2">
                                        Цена 
                                    </div>
                                </div>
                            </div>
                            <div class="bg-gray-200 rounded-lg text-gray-700 text-base md:text-lg text-center  md:px-4 py-2 m-2">{{ flat.price }}$</div>
                        </div>
                    </div>

                    <div v-if="flat.building.ways_from_metro != null && flat.building.ways_from_metro.length > 0" class=" rounded-lg  mt-5 shadow-sm md:transition md:duration-500 md:hover:shadow-md" >
                        <div class="px-2 py-2">
                            <div class="text-gray-700 text-base text-center">
                                <div class="inline-flex items-center">
                                    <highway-icon class="text-myMint-400" 
                                        />
                                    <div class="flex-1 m-1 md:m-2 px-4 p-2">
                                        Пути от метро
                                    </div>
                                </div>
                            </div>
                            <div class="flex-1 text-center">
                                <div class="w-full rounded-lg bg-gray-200 text-gray-700 text-base md:text-lg flex justify-center mt-2 lg:px-4 pb-2 pt-2" v-for="way in flat.building.ways_from_metro" :key="way.metro">
                                    <div class="w-2/5"> {{ way.metro }} </div>
                                    <div class="w-1/5"> {{ way.type_of_movement }} </div>
                                    <div class="w-1/5"> {{ way.time }} мин. </div>
                                    <div class="w-1/5"> {{ way.number_of_meters }} м. </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>              
            </div>
        </div>
    </modal>
</template>

<script>
import vPreviewSlider from './v-preview-slider'
import HighwayIcon from 'vue-material-design-icons/Highway.vue';
import HouseEditIcon from 'vue-material-design-icons/HomeEdit';
import HomeCityIcon from 'vue-material-design-icons/HomeCity';
import HomeGroupIcon from 'vue-material-design-icons/HomeGroup';
import DomainIcon from 'vue-material-design-icons/Domain';
import DoorIcon from 'vue-material-design-icons/Door'
import HomeFloor0Icon from 'vue-material-design-icons/HomeFloor0'
import RulerIcon from 'vue-material-design-icons/Ruler'
import CashUsdOutlineIcon from 'vue-material-design-icons/CashUsdOutline'
// import TelegramButton from "vue-share-buttons/src/components/TelegramButton";
// import ViberButton from "vue-share-buttons/src/components/ViberButton";
// import VkontakteButton from "vue-share-buttons/src/components/VkontakteButton";
// import ShareVariantIcon from 'vue-material-design-icons/ShareVariant'
import vShareDropdown from './v-share-dropdown'

export default {
    components:{
        vPreviewSlider,
        HighwayIcon,
        HouseEditIcon,
        HomeCityIcon,
        HomeGroupIcon,
        DomainIcon,
        DoorIcon,
        HomeFloor0Icon,
        RulerIcon,
        CashUsdOutlineIcon,
        // TelegramButton,
        // ShareVariantIcon,
        // ViberButton,
        // VkontakteButton,
        vShareDropdown
        // VueTabs,
        // VTab
    },
    props:{
        flat: {
            type: Object,
        }
    },
    methods: {
        // copyAddress () {
        //     let testingCodeToCopy = this.$refs.pageUrl
        //     testingCodeToCopy.setAttribute('type', 'text')    // 不是 hidden 才能複製
        //     testingCodeToCopy.select()
        //     // alert(testingCodeToCopy)
        //     try {
        //         // document.execCommand('copy');
        //         var successful = document.execCommand('copy');
        //         if(successful){
        //             this.addressCopiedSuccessfully = true
        //             setTimeout(()=>{
        //                 this.addressCopiedSuccessfully = false
        //             }, 
        //             1000);
        //             // alert()
        //         }
        //         if(!successful){
        //             this.addressCopiedUnsuccessfully = true
        //             setTimeout(()=>{
        //                 this.addressCopiedUnsuccessfully = false
        //             }, 
        //             1000);
        //         }
        //         // var msg = successful ? 'successful' : 'unsuccessful';
        //         // alert('Testing code was copied ' + msg);
        //     } catch (err) {
        //         // alert('Oops, unable to copy');
        //     }

        //     /* unselect the range */
        //     testingCodeToCopy.setAttribute('type', 'hidden')
        //     window.getSelection().removeAllRanges()
        //     },
    },
    data(){
        return{
            modalWidth:1000,
            // modalHeight:800,
            modalHeight:'auto',
            // socialMouseHover: false,
            // addressCopiedSuccessfully: false,
            // addressCopiedUnsuccessfully:false,

            
        }
    },
    computed: {
        sliderImages: function (){
            let images = []
            this.flat.flat_images.forEach(function(entry) {
                images.push(entry.flat_image)
            });
            this.flat.flat_layouts.forEach(function(entry) {
                images.push(entry.flat_layout)
            });
            return images
        },
        pageUrl: function(){ 
            let url = this.$router.resolve({ 
                name: 'flat-page',
                params: { slug:this.flat.building.slug, id:this.flat.id },
            }).href
            return window.location.origin + "/" + url
        },
        fullFlatAddress: function(){
            let house_letter = this.flat.building.house_letter != null ? this.flat.building.house_letter : ''
            // alert(house_letter)
            // console.log(house_letter)
            return this.flat.building.street + ' ' + this.flat.building.house_number + house_letter
        }
    },
    // mounted() {
    //     this.$smoothElement({
    //         el: this.$refs.textContainer,
    //         hideOverflow: true
    //     })
    //     // alert()
    // },

}
</script>

<style scoped>
    /* .vm--overlay {
    background: red;
    } */
    /* .share-button__icon{
        height: 20px;
    } */
</style>
