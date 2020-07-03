
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
                                <div class="text-2xl">
                                    <p class="uppercase font-bold text-gray-700">ЖК {{ building.name }}</p>
                                    <p class="text-gray-700 font-bold">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
                                </div>
                                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-6 pt-6">
                                    <div class="">
                                        <img v-if="building.building_images[0]" :src="building.building_images[0].building_image" class="cursor-pointer" @click="openMainImage"  alt="Главное фото">
                                        <img v-else-if="building.layout_images[0]" :src="building.layout_images[0].layout_image" class="cursor-pointer" @click="openMainImage"  alt="Главное фото">
                                        <img v-else :src="require('@/assets/images/no-photo-yet.jpg')" class="cursor-pointer" @click="openMainImage" alt="Главное фото">
                                    </div>
                                    <div class="col-span-1">
                                        <div class= 'h-full w-full'>

                                            <div class="grid grid-cols-2 justify-center text-center justify-center gap-2">
                                                <div v-if="building.administrative_district != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center text-wh">
                                                            <HomeCityIcon class="text-myMint-400" :size="30"  />
                                                            <div class="block xl:hidden flex-1 px-1  ">
                                                                Админ. район
                                                            </div>
                                                            <div class="hidden xl:block flex-1 px-2  ">
                                                                Административный район
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="rounded-lg bg-gray-100  text-gray-700 text-base md:text-lg text-center md:px-4 py-2 m-2">{{ building.administrative_district }}</div>
                                                </div>
                                                <div v-if="building.district != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <HomeGroupIcon class="text-myMint-400" :size="30" />
                                                            <div class="flex-1 sm:px-1 px-2">
                                                                Район
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="rounded-lg bg-gray-100 text-gray-700 text-base md:text-lg text-center md:px-4 py-2 m-2">{{ building.district }}</div>
                                                </div>
                                                <div v-if="building.micro_district !== 'Не делится на микрорайоны'" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <DomainIcon class="text-myMint-400" :size="30" />
                                                            <div class="flex-1 sm:px-1 px-2">
                                                                Микрорайон
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="bg-gray-100 rounded-lg text-gray-700 text-base md:text-lg  text-center md:px-4 py-2 m-1 md:m-2">{{ building.micro_district }}</div>
                                                </div>
                                                <div v-if="building.developer != null" class="flex-1 rounded-lg flex-col shadow-sm md:transition md:duration-500 md:hover:shadow-md">
                                                    <div class="text-gray-700 text-base text-center px-4 py-2 m-1 md:m-2">
                                                        <div class="inline-flex items-center">
                                                            <HouseEditIcon class="text-myMint-400" :size="30" />
                                                            <div class="flex-1 sm:px-1 px-2">
                                                                Застройщик
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="bg-gray-100 rounded-lg text-gray-700 text-base md:text-lg text-center  md:px-4 py-2 m-2">{{ building.developer }}</div>
                                                </div>
                                            </div>
                                            <div v-if="building.ways_from_metro != null && building.ways_from_metro.length > 0" class="flex1 rounded-lg  mt-5 shadow-sm md:transition md:duration-500 md:hover:shadow-md" >
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
                                                        <div class="w-full rounded-lg bg-gray-100 text-gray-700 text-base md:text-lg flex justify-center mt-2 lg:px-4 pb-2 pt-2" v-for="way in building.ways_from_metro" :key="way.metro">
                                                            <div class="w-2/5"> {{ way.metro }} </div>
                                                            <div class="w-1/5"> {{ way.type_of_movement }} </div>
                                                            <div class="w-1/5"> {{ way.time }} мин. </div>
                                                            <div class="w-1/5"> {{ way.number_of_meters }} м. </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div v-if="building.completion_date != null" class="flex1 rounded-lg mt-5 shadow-sm md:transition md:duration-500 md:hover:shadow-md" >
                                               <div class="px-2 py-2">
                                                <div class="text-gray-700 text-base text-center px-4 py-2 m-2">
                                                    <div class="inline-flex items-center">
                                                        <ClipboardCheckMultipleIcon class="text-myMint-400" :size="30" />
                                                        <div class="flex-1 px-2">
                                                            Сдан в эксплуатацию
                                                        </div>
                                                    </div>
                                                </div>
                                                    <div class="rounded-lg bg-gray-100 text-gray-700 text-base md:text-lg text-center md:px-4 py-2 ">{{ building.completion_date }}</div>
                                                </div>
                                            </div>
                                         </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                          <div id="building-on-map" class="mt-16 mb-16" v-if="building.lat && building.lng">

                                        <div class="md:flex md:-mx-2">
                                            <div class="m-auto w-4/5 md:px-2">
                                                <div class="hidden md:block">
                                                    <vMap :lat="building.lat" :lng="building.lng" :mapSize="500" :zoom="30"></vMap>
                                                </div>
                                                <div class="block md:hidden">
                                                    <vMap :lat="building.lat" :lng="building.lng" :mapSize="200" :zoom="30"></vMap>
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


<!-- <div class='p-10'> -->
    <div ref="anchors-default-position" class="invisible"> </div>
    <div ref="anchors" class="sticky text-center bg-myPageBackground top-0 pt-1 z-40 relative flex flex-col min-w-0 rounded-lg ">
        <div class="hidden md:block">
            <transition name="fade">
                    <div v-if="anchorsInfo.showAncorsTitle" class='flex-1 '>
                        <p class='text-center text-gray-700 text-lg '>{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</p>
                    </div>
                    <!-- <div v-else class='h-4'>
                    </div> -->
            </transition>
        </div>
        <scrollactive  :offset="90" active-class="activeScroll" :modifyUrl="false">
            <!-- <a href="#images" class="">Фото</a>
            <a href="#layouts" class="">Планировки</a> -->

            <ul class="flex text-sm md:text-base">
                <li class="flex-1 mx-1 md:mx-2">
                    <a href="#building-full-info" class="rounded-lg scrollactive-item bg-myHeaderColor text-white  md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-500 md:hover:shadow-xl py-2 ">
                        Об обьекте
                    </a>
                </li>
                <li class="flex-1 mx-1 md:mx-2">
                    <a href="#images" class="rounded-lg  scrollactive-item bg-myHeaderColor text-white  md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-500 md:hover:shadow-xl py-2 ">
                        Фото
                    </a>
                </li>
                <li class="flex-1 mx-1 md:mx-2">
                    <a href="#for-sale" class="rounded-lg  scrollactive-item bg-myHeaderColor text-white  md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-500 md:hover:shadow-xl py-2 ">
                        В продаже
                    </a>
                </li>
                <!-- <li class="flex-1 md:mx-2">
                    <a href="#buildings-for-sale" class="rounded-lg scrollactive-item bg-myHeaderColor text-white text-sm md:text-xl md:transition md:duration-500 md:transform md:hover:-translate-y-1 md:ease-in-out text-center block md:hover:bg-myMint-500 md:hover:shadow-xl py-2 ">
                        В продаже
                    </a>
                </li> -->
            </ul>
        </scrollactive>
    </div>
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
                                    <div id="building-full-info" class="mt-20 border-t md:rounded-lg md:transition md:duration-500 md:transform " >
                                        <div class="">
                                            <!-- <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myHeaderColor opacity-25"></div> -->
                                            <h2 class="text-2xl lg:pt-0 text-gray-700  rounded-lg text-center">Характеристики ЖК</h2>
                                            <!-- <div class="flex w-full"> -->
                                            <!-- <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myHeaderColor opacity-25"></div> -->
                                            <!-- </div> -->
                                            <div class='bg-white text-xs sm:text-sm md:text-base shadow-md rounded-lg mt-8 py-6 px-6'>
                                                <div class="grid grid-cols-2 ">
                                                    <div v-if="building.the_class">Класс:<span class="px-4 font-bold text-myMint-400">{{ building.the_class }}</span></div>
                                                    <div v-if="building.construction_technology">Технология строительства:<span class="px-4  font-bold text-myMint-400">{{ building.construction_technology }}</span></div>
                                                    <div v-if="building.number_of_storeys">Этажность:<span class="px-4  font-bold text-myMint-400">{{ building.number_of_storeys }}</span></div>
                                                    <div v-if="building.walls_type">Стены:<span class="px-4  font-bold text-myMint-400">{{ building.walls_type }}</span></div>
                                                    <div v-if="building.number_of_buildings">Кол-во домов:<span class="px-4  font-bold text-myMint-400">{{ building.number_of_buildings }}</span></div>
                                                    <div v-if="building.warming">Утепление:<span class="px-4  font-bold text-myMint-400">{{ building.warming }}</span></div>
                                                    <div v-if="building.number_of_sections_or_entrances">Кол-во секций / подьездов:<span class="px-4  font-bold text-myMint-400">{{ building.number_of_sections_or_entrances }}</span></div>
                                                    <div v-if="building.room_height">Высота помещений:<span class="px-4  font-bold text-myMint-400">{{ building.room_height }}</span></div>
                                                </div>
                                                <div v-if="building.number_of_apartments_in_house || building.number_of_apartments_per_floor" class="pt-4">
                                                    <div v-if="building.number_of_apartments_in_house" class="col-span-2">Кол-во квартир в доме:<span class="px-4 font-bold text-myMint-400">{{ building.number_of_apartments_in_house }}</span></div>
                                                    <div v-if="building.number_of_apartments_per_floor" class="col-span-2">Кол-во квартир на этаж:<span class="px-4 font-bold text-myMint-400">{{ building.number_of_apartments_per_floor }}</span></div>
                                                </div>
                                                <div v-if=" building.number_of_one_room || 
                                                            building.number_of_two_room || 
                                                            building.number_of_three_room ||
                                                            building.number_of_four_room"
                                                    class="pt-4"
                                                >
                                                    <p>ТИПЫ КВАРТИР:</p>
                                                    <div class="px-4">
                                                        <div v-if="building.number_of_one_room">1 комнатные квартиры |  кол-во: <span class="px-4  font-bold text-myMint-400">{{ building.number_of_one_room }}</span> каждая по <span class="pl-4  font-bold text-myMint-400">{{ building.square_of_one_room }} м<sup>2</sup></span></div>
                                                        <div v-if="building.number_of_two_room">2 комнатные квартиры |  кол-во: <span class="px-4  font-bold text-myMint-400">{{ building.number_of_two_room }}</span> каждая по <span class="pl-4  font-bold text-myMint-400">{{ building.square_of_two_room }} м<sup>2</sup></span></div>
                                                        <div v-if="building.number_of_three_room">3 комнатные квартиры |  кол-во: <span class="px-4  font-bold text-myMint-400">{{ building.number_of_three_room }}</span> каждая по <span class="pl-4  font-bold text-myMint-400">{{ building.square_of_three_room }} м<sup>2</sup></span></div>
                                                        <div v-if="building.number_of_four_room">4 комнатные квартиры |  кол-во: <span class="px-4  font-bold text-myMint-400">{{ building.number_of_four_room }}</span> каждая по <span class="pl-4  font-bold text-myMint-400">{{ building.square_of_four_room }} м<sup>2</sup></span></div>
                                                    </div>
                                                </div>
                                                <div class="pt-4">
                                                    <p>КОММЕРЧЕСКИЕ ПОМЕЩЕНИЯ:</p>
                                                    <div class="pl-4">
                                                        <div v-if="building.commercial_premises"><span class="px-4  font-bold text-myMint-400">{{ building.commercial_premises }}</span></div>
                                                    </div>
                                                </div>
                                                <div class="pt-4 grid grid-cols-2">
                                                    <div>
                                                        <p>КОММУНИКАЦИИ:</p>
                                                        <div class="pl-4">
                                                            <div v-if="building.heating">Отопление: <span class="px-4  font-bold text-myMint-400"> {{ building.heating}} </span></div>   
                                                            <div v-if="building.gasification">Газификация: <span class="px-4  font-bold text-myMint-400"> {{ building.gasification}} </span></div> 
                                                            <div>Водоснабжение????</div> 
                                                            <div>Электроенргия???</div>
                                                        </div>
                                                    </div>
                                                    <div>
                                                        <p>ЛИФТ:</p>
                                                        <div class="pl-4">
                                                            <div v-if="building.elevator"><span class="px-4  font-bold text-myMint-400">{{ building.elevator }}</span></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div id="images" class="mt-32 border-t" >
                                        <h2 class="text-2xl lg:pt-0 text-gray-700 text-center">Изображения дома</h2>
                                        <!-- <div class="flex w-full"> -->
                                        <!-- <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myHeaderColor opacity-25"></div> -->
                                        <!-- </div> -->
                                        <div class="mt-8 ">
                                            <building-gallary 
                                                v-if="building.building_images.length > 0"
                                                ref="buildings" 
                                                gallaryRef="buildingsGallary" 
                                                :images_src="building_images" 
                                                caption="Изображение дома"
                                            >
                                            </building-gallary>

                                            <building-gallary 
                                                v-else
                                                ref="buildings" 
                                                gallaryRef="buildingsGallary" 
                                                :images_src="[require('@/assets/images/no-photo-yet.jpg')]" 
                                                caption="Кошечка лучше, чем ничего"
                                            >
                                            </building-gallary>
                                        </div>
                                    </div>
                                    <div id="layouts" class="mt-32 border-t">
                                        <h2 class="text-2xl lg:pt-0 text-gray-700 text-center">Планировки</h2>
                                        <!-- <div class="flex w-full"> -->
                                            <!-- <div class="m-auto w-3/5 pt-3 mb-3 border-b-2 border-myHeaderColor opacity-25"></div> -->
                                        <!-- </div> -->
                                        <div class="mt-8">
                                            <building-gallary 
                                            v-if="building.layout_images.length > 0"
                                            ref="layouts"
                                            gallaryRef="layoutsGallary" 
                                            :images_src="layout_images" 
                                            caption="Планировка">
                                            </building-gallary>

                                            <building-gallary 
                                                v-else
                                                ref="layouts" 
                                                gallaryRef="layoutsGallary" 
                                                :images_src="[require('@/assets/images/no-photo-yet.jpg')]" 
                                                caption="Кошечка лучше, чем ничего"
                                            >
                                            </building-gallary>
                                        </div>
                                    </div>
                                    <div id="for-sale" class="mt-32 border-t" >
                                        <h2 class="text-2xl lg:pt-0 text-gray-700 text-center">Квартиры в продаже</h2>
                                        <div v-if="building.flats_for_sale.length > 0" class="mt-8 relative">
                                            <vForSaleSlider :flatsIdForSale="building.flats_for_sale"/>
                                        </div>
                                        <div v-else class="mt-16 mb-16 text-myHeaderColor">
                                            К сожалению, в этом доме нет квартир на продажу.
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
import BuildingGallary from '../components/v-building-gallary'
import { baseApiAddress } from '../variables'
// import vHeaderLittle from '../components/v-header-little'
import HighwayIcon from 'vue-material-design-icons/Highway.vue';
import HouseEditIcon from 'vue-material-design-icons/HomeEdit';
import HomeCityIcon from 'vue-material-design-icons/HomeCity';
import HomeGroupIcon from 'vue-material-design-icons/HomeGroup';
import DomainIcon from 'vue-material-design-icons/Domain';
import ClipboardCheckMultipleIcon from 'vue-material-design-icons/ClipboardCheckMultiple';
// import KeyboardBackspaceIcon from 'vue-material-design-icons/KeyboardBackspace'
import vMap from '../components/v-page-map'
import vBackButton from '../components/v-back-button'
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
        BuildingGallary,
        vMap,
        // vHeaderLittle,
        HighwayIcon,
        HouseEditIcon,
        HomeCityIcon,
        HomeGroupIcon,
        DomainIcon,
        ClipboardCheckMultipleIcon,
        vBackButton,
        vForSaleSlider
        // KeyboardBackspaceIcon,
        // vBackToTopButton
        // vGoogleMapModal,
        // VueScrollactive
    },
    data(){
        return{
            building: {},
            loading: false,
            anchorsInfo: {showAncorsTitle: false},
            // prevRoute: null,
            // currentWindowOffset: window.pageYOffset,
            // fullWindowHeight:window.innerHeight ,
            readMoreActivated: false,
            textAboutMap: `P.S. Так как мы используем бесплатную карту, новострои могут не отображаться на карте должным образом (маркер может указывать на место, которое никак не обозначено на карте). Однако сам маркер имеет точные координаты дома, проверенные Google. 
                            Чтобы ознакомиться с полной инфраструктурой Вы можете воспользоваться кнопкой "Открыть в Google maps". Просим прощения за неудобства`
        }
        
    },
    // beforeRouteEnter(to, from, next) {
    //     next(vm => {
    //         vm.prevRoute = from
    //         // console.log('FFFFFFFf')
    //         // console.log(from)
    //         // console.log(vm.$route)
    //         // console.log(vm.$router)
    //         // alert(vm.prevRoute.path)
    //     })
    // },
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
    created () {
         window.addEventListener('scroll', this.handleScroll);
         window.addEventListener('resize', this.updateAnchorsOffset);
            // this.anchorsOffsetTop = this.$refs.anchors.$el.offsetTop;
            // alert(this.anchorsOffsetTop)

    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll);
        window.removeEventListener('resize', this.updateAnchorsOffset);
    },

    methods: {
        async prepareData(){
            await this.searchBuilding()
        },

        async searchBuilding(){
            // const qs = require('qs');
            const axios = require('axios');
            await axios.get(baseApiAddress+'buildings/'+this.$route.params.slug, {
            // params: {
            //     slug:this.$route.params.slug
            //     }
            }).then(resp => {
            this.building = resp.data
            
            // const foundBuildings = resp.data.results
            // const buildingsCount = resp.data.count
            // console.log('FOUND BUILDINGS')
            // console.log(foundBuildings)
            // ctx.commit('updateBuildings', foundBuildings)
            // ctx.commit('updateBuildingsCount', buildingsCount)
            })
            console.log(this.building)
        },
        openMainImage(){
            console.log("Вот так вот:")
            console.log(this.$refs.buildings.$refs.buildingsGallary.$el)
            if (this.building_images.length > 0){
                this.$refs.buildings.$refs.buildingsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
            }
            else if(this.layout_images.length > 0){
                this.$refs.layouts.$refs.layoutsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
            }
            else{
                this.$refs.buildings.$refs.buildingsGallary.$el.querySelector('a[itemprop="contentUrl"]').click()
            }
        },
        // ---- for animation eg
        handleScroll () {
            // this.currentWindowOffset = window.pageYOffset

            if(!this.anchorsInfo.defaultPosition && this.$refs["anchors-default-position"]){
                this.anchorsInfo.defaultPosition = this.$refs["anchors-default-position"].offsetTop 
            }
            // console.log('SCROLE: ')
            // console.log(window.pageYOffset)
            // console.log(this.anchorsInfo.defaultPosition)
            if (window.pageYOffset > this.anchorsInfo.defaultPosition) {
                this.anchorsInfo.showAncorsTitle = true
                // this.anchorsInfo.element.classList.add("text-center");

            } else {
                this.anchorsInfo.showAncorsTitle = false
                // this.anchorsInfo.element.classList.remove("text-center");
            }
        },
        updateAnchorsOffset(){
            // this.fullWindowHeight = window.innerHeight

            this.anchorsInfo.element = this.$refs.anchors;
            // this.anchorsInfo.anchorsOffset = this.anchorsInfo.element.offsetTop
            // console.log("Anchors offset: "+this.anchorsInfo.anchorsOffset)
            this.anchorsInfo.defaultPosition = this.$refs["anchors-default-position"].offsetTop 
            // alert( this.anchorsInfo.defaultPosition)
            this.handleScroll()
            // console.log("Default anchor position"+this.anchorsInfo.defaultPosition)
        },
        // showGoogleMapsModal(){
        //     this.$modal.show('google-map-modal');
        // },
        openInGoogleMaps(){
            // let house_letter = this.building.house_letter ? this.building.house_letter : ''
            // let address = `https://www.google.com/maps/search/?api=1&query=${this.building.street}+${this.building.house_number}+${house_letter}`
            window.open(this.googleMapUrl, '_blank')

            // this.$modal.show('google-map-modal');
            // console.log('REFFFFFSSSS')
            // console.log(this.$refs.googleModalMapComponent.$refs.googleMapModal.$refs)
            //  this.$refs.googleModalMapComponent.$refs.modalBody.$el = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" src="'+this.url+'"></iframe>';
        },
        openInGoogleStreetView(){
            window.open(this.googleStreetUrl, '_blank')
        }
        // updateGallaryClass(){
        //     let gallaries = document.querySelectorAll('my-gallery');
        //     gallaries.forEach(
        // }
    },
      computed: {
        building_images: function (){
            let images = []
            this.building.building_images.forEach(function(entry) {
                images.push(entry.building_image)
            });
            return images
        },
        layout_images: function () {
            let images = []
            this.building.layout_images.forEach(function(entry) {
                images.push(entry.layout_image)
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
            let house_letter = this.building.house_letter ? this.building.house_letter : '';
            return `https://www.google.com/maps/search/?api=1&query=${this.building.street}+${this.building.house_number}+${house_letter}`;
        },
        googleStreetUrl(){
            // let house_letter = this.building.house_letter ? this.building.house_letter : '';
            return `https://www.google.com/maps/@?api=1&map_action=pano&viewpoint=${this.building.lat},${this.building.lng}`;
            // https://www.google.com/maps/@?api=1&map_action=pano&viewpoint=48.857832,2.295226&heading=-45&pitch=38&fov=80
        
        },
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
