
<template>
    <div v-if="loading">
    <!-- <section class="pb-20 -mt-32"> -->
        <!-- <vHeaderLittle/> -->
        <section class="pb-20 -mt-24 ">
            <div class="container mx-auto md:px-8">

                <div class="flex flex-wrap ">
                    
                        <!-- <div @click="$router.back(-1)" class=" invisible md:visible cursor-pointer w-auto left-0 bg-red-300">
                            <div class='ml-2 mr-2 text-2xl text-white text-center'>
                                Назад
                            </div>
                        
                        </div> -->
                    <div class="w-full"> 
                        <!-- <div @click="$router.back(-1)" class=" invisible md:visible cursor-pointer w-auto left-0 bg-red-300">
                            <div class='ml-2 mr-2 text-2xl text-white text-center'>
                                Назад
                            </div>
                        </div> -->
                        <vBackButton/>
                        <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg">
                            <div class="px-1 md:px-4 py-5 flex-auto">
                                <div class="flex justify-between">
                                    <div class="text-2xl">
                                        <p class="uppercase font-bold text-gray-700">{{ flat.description }}</p>
                                        <p class="text-gray-700 font-bold">{{ flat.building.street }} {{ flat.building.house_number }}{{ flat.building.house_letter }}</p>
                                    </div>
                                    <div class="text-2xl text-myMint-400 my-auto p-5 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                        <span>Цена: {{ flat.price }} $ </span>
                                    </div>
    
                                </div>
                                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-6 pt-6">
                                    <div class="">
                                        <img v-if="flat.flat_images[0]" :src="flat.flat_images[0].flat_image" class="cursor-pointer" @click="openMainImage"  alt="Главное фото">
                                        <img v-else-if="flat.flat_layouts[0]" :src="flat.flat_layouts[0].flat_layout" class="cursor-pointer" @click="openMainImage"  alt="Главное фото">
                                        <img v-else :src="require('@/assets/images/no-photo-yet.jpg')" class="cursor-pointer" @click="openMainImage" alt="Главное фото">
                                    </div>
                                    <div class="col-span-1">
                                        <div class= 'h-full w-full'>

                                            <div class="grid grid-cols-2 justify-center text-center justify-center gap-2">
                                                <div v-if="flat.building.district != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <CityIcon class="text-myMint-400" :size="30" />
                                                            <div class="flex-1 sm:px-1 px-2">
                                                                Расположение
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="rounded-lg bg-gray-100 text-gray-700 text-sm text-center md:px-4 py-2 m-2">
                                                            Харьков
                                                            <span v-if="flat.building.administrative_district != null">, {{ flat.building.administrative_district}}</span>
                                                            <span v-if="flat.building.district != null">, {{flat.building.district}}</span>
                                                            <span v-if="flat.building.street != null">, {{ flat.building.street }}</span>
                                                            <span v-if="flat.building.house_number != null">, {{ flat.building.house_number }}</span>
                                                            <span v-if="flat.building.house_letter != null">{{ flat.building.house_letter }}</span>
                                                        </div>
                                                </div>
                                                <div v-if="flat.rooms != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center text-wh">
                                                            <DoorIcon class="text-myMint-400" :size="30"  />
                                                            <div class="flex-1 px-2  ">
                                                                Комнат
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="rounded-lg bg-gray-100  text-gray-700 text-base md:text-lg text-center md:px-4 py-2 m-2">{{ flat.rooms }}</div>
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
                                                    <div class="rounded-lg bg-gray-100 text-gray-700 text-base md:text-lg text-center md:px-4 py-2 m-2">{{ flat.floor }}/{{ flat.building.number_of_storeys }}</div>
                                                </div>
                                                <div v-if="flat.living_area !== 'Не делится на микрорайоны'" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <RulerIcon class="text-myMint-400" :size="30" />
                                                            <div class="flex-1 sm:px-1 px-2">
                                                                S общ/жил/кух:  
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div v-if="flat.kitchen_area" class="bg-gray-100 rounded-lg text-gray-700 text-base md:text-lg  text-center md:px-4 py-2 m-1 md:m-2">{{ flat.living_area + flat.kitchen_area }}/{{ flat.living_area }}/{{ flat.kitchen_area }} м<sup>2</sup> </div>
                                                    <div v-else class="bg-gray-100 rounded-lg text-gray-700 text-base md:text-lg  text-center md:px-4 py-2 m-1 md:m-2">{{ flat.living_area }}/{{ flat.living_area }}/- м<sup>2</sup></div>
                                                </div>
                                               
                                            </div>
                                            <div v-if="flat.building.ways_from_metro != null && flat.building.ways_from_metro.length > 0" class="flex1 rounded-lg  mt-5 shadow-sm md:transition md:duration-500 md:hover:shadow-md" >
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
                                                        <div class="w-full rounded-lg bg-gray-100 text-gray-700 text-base md:text-lg flex justify-center mt-2 lg:px-4 pb-2 pt-2" v-for="way in flat.building.ways_from_metro" :key="way.metro">
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
                                 <div class="rounded-lg  mt-5 shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                    <div class="px-2 py-2">
                                        <div class="text-gray-700 text-base text-center">
                                            <div class="inline-flex items-center">
                                                <highway-icon class="text-myMint-400" 
                                                    />
                                                <div class="flex-1 m-1 md:m-2 px-4 p-2">
                                                    Описание:
                                                </div>
                                            </div>
                                        </div>
                                        <div class="bg-gray-100 rounded-lg text-gray-700 text-base md:text-lg  text-center md:px-4 py-2 m-1 md:m-2">
                                            {{ flat.description }}
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-end pt-2">
                                    <vShareDropdown/>
                                </div>
                            </div>
                        </div>
                            <div class="flex">
                                <p class="p-4">
                                    Перейдите на страницу новостроя, в котором находится эта квартира, чтобы подробно изучить его
                                </p>
                                <router-link :to="{name:'building-page', params:{slug:flat.building.slug}}">
                                    <div class="ml-4 p-4 border bg-myHeaderColor text-white rounded-lg md:transition md:duration-500 md:transform md:hover:translate-x-2 md:hover:bg-myMint-400">
                                        Перейти
                                    </div>
                                </router-link>
                            </div>
                          <div id="building-on-map" class="mt-16 mb-16" v-if="flat.building.lat && flat.building.lng">

                                        <div class="md:flex md:-mx-2">
                                            <div class="m-auto w-4/5 md:px-2">
                                                <div class="hidden md:block">
                                                    <vMap :lat="flat.building.lat" :lng="flat.building.lng" :mapSize="500" :zoom="30"></vMap>
                                                </div>
                                                <div class="block md:hidden">
                                                    <vMap :lat="flat.building.lat" :lng="flat.building.lng" :mapSize="200" :zoom="30"></vMap>
                                                </div>
                                            </div>
                                            <div class="w-full md:w-auto grid grid-cols-2 md:grid-cols-none md:grid-rows-2 px-6 md:px-2 gap-2">
                                                <div @click="openInGoogleMaps" class="flex border cursor-pointer rounded-lg  text-black shadow md:text-xl md:transition md:duration-500 md:transform md:hover:translate-x-2 md:ease-in-out text-center block  md:hover:shadow-xl py-2">
                                                    <div class="m-auto">
                                                        Открыть в Google Maps
                                                    </div>
                                                </div>
                                                <div @click="openInGoogleStreetView" class="flex border cursor-pointer rounded-lg  text-black shadow md:text-xl md:transition md:duration-500 md:transform md:hover:translate-x-2 md:ease-in-out text-center block md:hover:shadow-xl py-2">
                                                    <div class="m-auto">
                                                        Покрутить в Google Streets View
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="text-sm pt-4 pl-2 pr-2">
                                            <p v-if="!readMoreActivated">{{textAboutMap.slice(0, 60)}}...
                                                <span class="pl-2 text-center text-myMint-400 cursor-pointer" @click="readMoreActivated = !readMoreActivated">
                                                    Читать далее
                                                </span>
                                            </p>
                                            <p v-if="readMoreActivated">
                                                {{ textAboutMap }}
                                                <span class="pl-2 text-center text-myMint-400 cursor-pointer" @click="readMoreActivated = !readMoreActivated">
                                                    Скрыть
                                                </span>
                                            </p>

                                            <!-- {{ textAboutMap }} -->
                                        </div>
                            </div>
                            <div v-else id="building-on-map" class="mt-16 mb-16 font-bold text-myHeaderColor">
                                К сожалению, новострой еще не достроился и не имеет адресса, который может быть отображен на карте :(
                            </div>


    <!-- <div ref="anchors-default-position" class="invisible"> </div>
    <div ref="anchors" class="sticky text-center bg-myPageBackground top-0 pt-1 z-40 relative flex flex-col min-w-0 rounded-lg ">
        <div class="hidden md:block">
            <transition name="fade">
                    <div v-if="anchorsInfo.showAncorsTitle" class='flex-1 '>
                        <p class='text-center text-gray-700 text-lg '>{{ flat.building.street }} {{ flat.building.house_number }}{{ flat.building.house_letter }}</p>
                    </div>

            </transition>
        </div>
        <scrollactive  :offset="90" active-class="activeScroll" :modifyUrl="false">


            <ul class="flex text-sm md:text-base">

                <li class="flex-1 mx-1 md:mx-2">
                    <a href="#images" class="rounded-lg  scrollactive-item bg-myHeaderColor text-white  md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-500 md:hover:shadow-xl py-2 ">
                        Изображения
                    </a>
                </li>
                <li class="flex-1 mx-1 md:mx-2">
                    <a href="#layouts" class="rounded-lg  scrollactive-item bg-myHeaderColor text-white  md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-500 md:hover:shadow-xl py-2 ">
                        Планировки
                    </a>
                </li>

            </ul>
        </scrollactive>
    </div> -->
<!-- </div> -->
  <!-- <div class="flex h-16 bg-myMint-400 text-white hover:bg-myMint-100 hover:text-black transition duration-500 ease-in-out hover:rounded-none hover:opacity-40 transform hover:translate-y-1 hover:shadow-2xl overflow-hidden shadow-md">  
                        <p class="m-auto text-xl"> Открыть полностью </p>
                    </div> -->
    

                    
                        <!-- <div
                            class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
                        > -->
                        <div
                            class="relative flex flex-col min-w-0 w-full pt-8 mb-8 rounded-lg"
                        >
                            <div class="flex-auto">
                                <div>
                                    
                                    <div id="images" class=" border-t" >
                                        <h2 class="text-2xl lg:pt-0 text-gray-700 text-center">Изображения квартиры</h2>
                                        <!-- <div class="flex w-full"> -->
                                        <!-- <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myHeaderColor opacity-25"></div> -->
                                        <!-- </div> -->
                                        <div class="mt-8 ">
                                            <flat-gallary
                                                v-if="flat.flat_images.length > 0"
                                                ref="flats" 
                                                gallaryRef="flatsGallary" 
                                                :images_src="flat_images" 
                                                caption="Изображение квартиры"
                                            >
                                            </flat-gallary>

                                            <flat-gallary 
                                                v-else
                                                ref="flats" 
                                                gallaryRef="flatsGallary" 
                                                :images_src="[require('@/assets/images/no-photo-yet.jpg')]" 
                                                caption="Мы уже работаем над этим!"
                                            >
                                            </flat-gallary>
                                        </div>
                                    </div>
                                    <div id="layouts" class="mt-32 border-t">
                                        <h2 class="text-2xl lg:pt-0 text-gray-700 text-center">Планировки</h2>
                                        <!-- <div class="flex w-full"> -->
                                            <!-- <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myHeaderColor opacity-25"></div> -->
                                        <!-- </div> -->
                                        <div class="mt-8">
                                            <flat-gallary 
                                            v-if="flat.flat_layouts.length > 0"
                                            ref="layouts"
                                            gallaryRef="layoutsGallary" 
                                            :images_src="flat_layouts" 
                                            caption="Планировка">
                                            </flat-gallary>

                                            <flat-gallary 
                                                v-else
                                                ref="layouts" 
                                                gallaryRef="layoutsGallary" 
                                                :images_src="[require('@/assets/images/no-photo-yet.jpg')]" 
                                                caption="Мы уже работаем над этим!"
                                            >
                                            </flat-gallary>
                                        </div>
                                    </div>
                                    <div id="for-sale" class="mt-32 border-t" >
                                        <h2 class="text-2xl lg:pt-0 text-gray-700 text-center">В этом доме так же продаются</h2>
                                        <div v-if="actualFlatsForSale.length > 0" class="mt-8 relative">
                                            <vForSaleSlider :flatsIdForSale="actualFlatsForSale"/>
                                        </div>
                                        <div v-else class="mt-16 mb-16 text-myHeaderColor">
                                            К сожалению, в данном доме сейчас продается только эта квартира.
                                        </div>
                                    </div>
                                   <!-- <div id="building-on-map" class="mt-32 border-t" >
                                        <h2 class="text-2xl lg:pt-0 text-gray-700 text-center">Карта</h2>
                                        <div class="mt-6">
                                            <div class="cursor-pointer rounded-lg  text-black text-xl md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-500 md:hover:shadow-xl py-2">
                                                Открыть в GoogleMaps
                                            </div>
                                            <vMap :lat="building.lat" :lng="building.lng" :zoom="30"></vMap>
                                            <div class="text-sm">
                                            P.S. Так как мы используем бесплатную карту, новострои могут не отображаться на карте должным образом (маркер может указывать на место, которое никак не обозначено на карте). Однако сам маркер имеет точные координаты дома, проверенные Google. 
                                            Чтобы ознакомиться с полной инфраструктурой Вы можете воспользоваться кнопкой "Открыть в Google maps". Просим прощения за неудобства
                                            </div>
                                        </div>
                                    </div> -->

                                    <!-- <div id="buildings-for-sale" class="mt-32 border-t" >
                                        <h2 class="text-2xl lg:pt-0 text-gray-700 text-center">Обьекты в продаже</h2>
     
                                        <div class="mt-8">
        
                                        </div>
                                    </div> -->

                                    <!-- <div id="building-on-map" class="mt-16 mb-16">
                                        <div class="cursor-pointer rounded-lg  text-black text-xl md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-500 md:hover:shadow-xl py-2">
                                            Открыть в GoogleMaps
                                        </div>
                                         <vMap :lat="building.lat" :lng="building.lng" :zoom="30"></vMap>
                                        <div class="text-sm">
                                        P.S. Так как мы используем бесплатную карту, новострои могут не отображаться на карте должным образом (маркер может указывать на место, которое никак не обозначено на карте). Однако сам маркер имеет точные координаты дома, проверенные Google. 
                                        Чтобы ознакомиться с полной инфраструктурой Вы можете воспользоваться кнопкой "Открыть в Google maps". Просим прощения за неудобства
                                        </div>
                                    </div> -->
                                </div>
                                
                            </div>
                            <!-- <div v-else>
                                <building-gallary 
                                    ref="buildings" 
                                    gallaryRef="buildingsGallary" 
                                    :images_src="[require('@/assets/images/cat-no-photo-yet-green-2.jpg')]" 
                                    caption="Кошечка лучше, чем ничего"
                                >
                                </building-gallary>
                            </div> -->
                        </div>
                    </div>

                </div>
            </div>
        </section>
        <!-- <div class='z-50'>
            <vBackToTopButton :currentOffset="currentWindowOffset" :fullWindowHeight="fullWindowHeight"/>
        </div> -->
        <!-- <vGoogleMapModal ref='googleModalMapComponent' :url="googleMapUrl"/> -->
    </div>
    <!-- </section> -->
</template>

<script>
import FlatGallary from '../components/v-building-gallary'
import { baseApiAddress } from '../variables'
// import vHeaderLittle from '../components/v-header-little'
import HighwayIcon from 'vue-material-design-icons/Highway.vue';
// import HouseEditIcon from 'vue-material-design-icons/HomeEdit';
// import HomeCityIcon from 'vue-material-design-icons/HomeCity';
// import HomeGroupIcon from 'vue-material-design-icons/HomeGroup';
// import DomainIcon from 'vue-material-design-icons/Domain';
// import ClipboardCheckMultipleIcon from 'vue-material-design-icons/ClipboardCheckMultiple';
import CityIcon from 'vue-material-design-icons/City';
// import KeyboardBackspaceIcon from 'vue-material-design-icons/KeyboardBackspace'
import vMap from '../components/v-page-map'
import vBackButton from '../components/v-back-button'
import DoorIcon from 'vue-material-design-icons/Door'
import HomeFloor0Icon from 'vue-material-design-icons/HomeFloor0'
import RulerIcon from 'vue-material-design-icons/Ruler'
import vShareDropdown from '../components/v-share-dropdown'
import vForSaleSlider from '../components/v-for-sale-slider'
// import vBackToTopButton from '../components/v-back-to-top'
// import vGoogleMapModal from '../components/v-google-map'
// import debounce from 'lodash/debounce';
// import VueScrollactive from 'vue-scrollactive';


export default {
    // props:{
    //     slug:{
    //         type: String,
    //     }
    // },
    components:{
        FlatGallary,
        vMap,
        // vHeaderLittle,
        HighwayIcon,
        // HouseEditIcon,
        // HomeCityIcon,
        // HomeGroupIcon,
        // DomainIcon,
        // ClipboardCheckMultipleIcon,
        vBackButton,
        CityIcon,
        DoorIcon,
        HomeFloor0Icon,
        RulerIcon,
        vShareDropdown,
        vForSaleSlider
        // KeyboardBackspaceIcon,
        // vBackToTopButton
        // vGoogleMapModal,
        // VueScrollactive
    },
    data(){
        return{
            flat: {},
            loading: false,
            anchorsInfo: {showAncorsTitle: false},
            prevRoute: null,
            // currentWindowOffset: window.pageYOffset,
            // fullWindowHeight:window.innerHeight ,
            readMoreActivated: false,
            textAboutMap: `P.S. Так как мы используем бесплатную карту, новострои могут не отображаться на карте должным образом (маркер может указывать на место, которое никак не обозначено на карте). Однако сам маркер имеет точные координаты дома, проверенные Google. 
                            Чтобы ознакомиться с полной инфраструктурой Вы можете воспользоваться кнопкой "Открыть в Google maps". Просим прощения за неудобства`
        }
        
    },
    beforeRouteEnter(to, from, next) {
        next(vm => {
            vm.prevRoute = from
            // console.log('FFFFFFFf')
            // console.log(from)
            // console.log(vm.$route)
            // console.log(vm.$router)
            // alert(vm.prevRoute.path)
        })
    },
    mounted() {
        if(this.$route.params.slug === undefined){
            this.$router.replace({name: 'page-404' })
        }
        this.prepareData()
            .then(() => {
                this.loading = true
                // this.$nextTick(()=>{
                //     // this.updateAnchorsOffset()  
                //     alert(this.$refs["anchors-default-position"].offsetTop )
                // });
                
                }
            )   
    },
    // ------ For animation eg
    // created () {
    //      window.addEventListener('scroll', this.handleScroll);
    //      window.addEventListener('resize', this.updateAnchorsOffset);
    //         // this.anchorsOffsetTop = this.$refs.anchors.$el.offsetTop;
    //         // alert(this.anchorsOffsetTop)

    // },
    // destroyed () {
    //     window.removeEventListener('scroll', this.handleScroll);
    //     window.removeEventListener('resize', this.updateAnchorsOffset);
    // },

    methods: {
        async prepareData(){
            await this.searchFlats()
        },

        async searchFlats(){
            // const qs = require('qs');
            const axios = require('axios');
            await axios.get(baseApiAddress+'flats/'+this.$route.params.id, {
            // params: {
            //     slug:this.$route.params.slug
            //     }
            }).then(resp => {
            this.flat = resp.data
            // console.log(this.flat)
            // const foundBuildings = resp.data.results
            // const buildingsCount = resp.data.count
            // console.log('FOUND BUILDINGS')
            // console.log(foundBuildings)
            // ctx.commit('updateBuildings', foundBuildings)
            // ctx.commit('updateBuildingsCount', buildingsCount)
            })
            console.log('Квартиры: ',this.flat)
        },
        openMainImage(){
            console.log("Вот так вот:")
            console.log(this.$refs.flats.$refs.flatsGallary.$el)
            if (this.flat_images.length > 0){
                this.$refs.flats.$refs.flatsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
            }
            else if(this.flat_layouts.length > 0){
                this.$refs.flats.$refs.layoutsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
            }
            else{
                this.$refs.flats.$refs.buildingsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
            }
        },
        // ---- for animation eg
        // handleScroll () {
        //     // this.currentWindowOffset = window.pageYOffset

        //     if(!this.anchorsInfo.defaultPosition && this.$refs["anchors-default-position"]){
        //         this.anchorsInfo.defaultPosition = this.$refs["anchors-default-position"].offsetTop 
        //     }
        //     // console.log('SCROLE: ')
        //     // console.log(window.pageYOffset)
        //     // console.log(this.anchorsInfo.defaultPosition)
        //     if (window.pageYOffset > this.anchorsInfo.defaultPosition) {
        //         this.anchorsInfo.showAncorsTitle = true
        //         // this.anchorsInfo.element.classList.add("text-center");

        //     } else {
        //         this.anchorsInfo.showAncorsTitle = false
        //         // this.anchorsInfo.element.classList.remove("text-center");
        //     }
        // },
        // updateAnchorsOffset(){
        //     // this.fullWindowHeight = window.innerHeight

        //     this.anchorsInfo.element = this.$refs.anchors;
        //     // this.anchorsInfo.anchorsOffset = this.anchorsInfo.element.offsetTop
        //     // console.log("Anchors offset: "+this.anchorsInfo.anchorsOffset)
        //     this.anchorsInfo.defaultPosition = this.$refs["anchors-default-position"].offsetTop 
        //     // alert( this.anchorsInfo.defaultPosition)
        //     this.handleScroll()
        //     // console.log("Default anchor position"+this.anchorsInfo.defaultPosition)
        // },
        // showGoogleMapsModal(){
        //     this.$modal.show('google-map-modal');
        // },
        openInGoogleMaps(){
            window.open(this.googleMapUrl, '_blank')
        },
        openInGoogleStreetView(){
            window.open(this.googleStreetUrl, '_blank')
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
        // updateGallaryClass(){
        //     let gallaries = document.querySelectorAll('my-gallery');
        //     gallaries.forEach(
        // }
    },
      computed: {
        flat_images: function (){
            let images = []
            this.flat.flat_images.forEach(function(entry) {
                images.push(entry.flat_image)
            });
            return images
        },
        flat_layouts: function () {
            let images = []
            this.flat.flat_layouts.forEach(function(entry) {
                images.push(entry.flat_layout)
            });
            return images
        },
        // canBack(){
        //     if(window.history.length > 1){
        //         return true
        //     }
        //     return false
        // },
        googleMapUrl(){
            let house_letter = this.flat.building.house_letter ? this.flat.building.house_letter : '';
            return `https://www.google.com/maps/search/?api=1&query=${this.flat.building.street}+${this.flat.building.house_number}+${house_letter}`;
        },
        googleStreetUrl(){
            // let house_letter = this.building.house_letter ? this.building.house_letter : '';
            return `https://www.google.com/maps/@?api=1&map_action=pano&viewpoint=${this.flat.building.lat},${this.flat.building.lng}`;
            // https://www.google.com/maps/@?api=1&map_action=pano&viewpoint=48.857832,2.295226&heading=-45&pitch=38&fov=80
        
        },
        actualFlatsForSale(){
            let actualFlats = this.flat.building.flats_for_sale
            var index = actualFlats.findIndex(item => item.id == this.flat.id);
            console.log('INDEX: ', index)
            if (index > -1) {
                actualFlats.splice(index, 1);
                return actualFlats
            }
            print('\tERROR! Данная квартира не находится в списке квартир на продажу!')
            return false
        }
        // currentWindowOffset(){
        //     return window.pageYOffset
        // }
    },
}
</script>

<style  scoped>
.fade-enter-active{
  transition: opacity .5s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}

.activeScroll{
    background: #006B53;
    color: white;
}

</style>
