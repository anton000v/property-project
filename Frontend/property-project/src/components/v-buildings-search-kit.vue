<template>

    <!-- <div :if="dataReady"> -->
    <!-- <div id="searchComponent" :class="{'collapsed' : !isExtendedSearchActivated}" class="flex flex-wrap"> -->
    <div class="flex flex-wrap">
      <div class="w-full text-center"> 
        <div
          class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"  
        >
          <div class="px-4 py-5 flex-auto" ref='searchComponent' >


                       <div class="flex flex-col-reverse flex-wrap md:flex-row">
                                <div class="w-1/3 hidden md:block"></div>
                                <div class="w-full md:w-1/3 pt-5 md:pt-0 justify-center  text-center" >
                                <!-- <div class="flex group cursor-pointer transition duration-500"
                                
                                > -->
                                    <div 
                                        ref="searchButton"
                                        v-on:click="search"
                                        class="inline-block text-white p-3 text-center items-center justify-center shadow-lg rounded-full transition duration-500 transform bg-myHeaderColor hover:text-myMint-300 cursor-pointer">
                                        <div>
                                        <HomeSearchIcon title="Принудительный поиск"/>
                                        </div>
                                    </div>
                                <!-- <div class="m-auto bg-myHeaderColor text-white p-1 -ml-2 rounded-r-lg">
                                    По карте
                                </div> -->
                                <!-- </div> -->
                            </div>
                            <div class="w-full md:w-1/3">
                                <p class="-my-4 text-sm">Попробуйте менее занудный</p>
                                <!-- <p class="text-xs block md:hidden">Можете выбрать</p> -->
                                <router-link :to="{name:'map-search'}">
                                <div  class="my-4 h-full group bg-myHeaderColor flex rounded-lg cursor-pointer transition duration-500 transform hover:translate-y-1 hover:shadow-xl">
                                    <div class="m-auto">
                                    <div class="flex"> 
                                        <GoogleMapsIcon class="m-auto text-white transition duration-500 group-hover:text-myMint-300"/>
                                        <p class="text-white pl-2 text-base p-2">Поиск по карте</p>
                                    </div>
                                    </div>
                                </div>
                                </router-link>
                            </div>
                        </div>


            <div class="flex flex-wrap -mx-3" >
              <div class="w-full md:w-1/2 px-3 pt-3 md:pt-6">
                <label class="hidden text-xs md:text-sm lg:text-base md:block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Административные районы
                </label>
                <label class="block text-xs md:text-sm lg:text-base md:hidden text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Админ. районы
                </label>
                <div name="field" class="w-full">
                  <MultipleSelect 
                  @selectClose="search"
                  :dbValueKey="administrativeDistrictsBaseVariables.dbValueKey"
                  :fieldChoiceText="administrativeDistrictsBaseVariables.choiceText" 
                  :dictKey="administrativeDistrictsBaseVariables.dictKey" 
                  :apiAddress="administrativeDistrictsBaseVariables.fullApiAddress" 
                  :sendParamName="administrativeDistrictsBaseVariables.sendParamName"
                  :addAction="addFindParam"
                  :removeAction="removeFindParam"
                  :removeKeyAction="removeFindParamKey"
                  placeholder="Московский, Киевский..." 
                  />
                </div>
              </div>
              <div class="w-full md:w-1/2 px-3 pt-3 md:pt-6">
                <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="inline-full-name">
                  Районы
                </label>
                <div class="w-full">
                  <div name="field" class="w-full">
                    <MultipleSelect 
                    @selectClose="search" 
                    @select="checkToShowMicroDistricts"
                    @remove="checkToHideMicroDistricts"
                    @removeAll="setDefaultDistrictsChoosen"
                    :dbValueKey="districtsBaseVariables.dbValueKey"
                    :extraInformationField="districtsBaseVariables.extraInformationText"
                    :fieldChoiceText="districtsBaseVariables.choiceText" 
                    :dictKey="districtsBaseVariables.dictKey" 
                    :sendParamName="districtsBaseVariables.sendParamName"
                    :apiAddress="districtsBaseVariables.fullApiAddress" 
                    :trackEveryUpdate="true"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    :removeKeyAction="removeFindParamKey"
                    placeholder="Центр, Салтовка..." 
                    />
                  </div>
                </div>
              </div>
            </div>
            <TransitionDownRide>
              <div class="flex flex-wrap -mx-3 pt-3 md:pt-6" v-if="isSaltovkaDistrictChoosen || isSevernayaSaltovkaDistrictChoosen">
                <div class='w-1/2'></div>
                <div class="w-full md:w-1/2 grid grid-cols-2" >  
                  <TransitionDownRide>
                    <div class="w-full text-sm lg:text-base px-3 mb-3 md:mb-0 " v-if="isSaltovkaDistrictChoosen">
                      <label class="block text-xs md:text-sm lg:text-base text-gray-500 md:font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                        Салтовка
                      </label>
                      <div name="field" class="w-full">
                        <MultipleSelect 
                        @selectClose="search"
                        :dbValueKey="saltovkaMicroDistrictsBaseVariables.dbValueKey"
                        :fieldChoiceText="saltovkaMicroDistrictsBaseVariables.choiceText" 
                        :dictKey="saltovkaMicroDistrictsBaseVariables.dictKey" 
                        :apiAddress="saltovkaMicroDistrictsBaseVariables.fullApiAddress" 
                        :sendParamName="saltovkaMicroDistrictsBaseVariables.sendParamName"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :removeKeyAction="removeFindParamKey"
                        placeholder="Микрорайоны" 
                        />
                      </div>
                    </div>
                  </TransitionDownRide>
                  <TransitionDownRide>
                    <div class="w-full px-3 pt-3 md:pt-6" v-if="isSevernayaSaltovkaDistrictChoosen">
                      <label class="hidden text-xs md:text-sm lg:text-base md:block text-sm md:text-base text-gray-500 md:font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                        Северная Салтовка.
                      </label>
                      <label class="block text-xs md:text-sm lg:text-base md:hidden text-sm md:text-base text-gray-500 md:font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                        Северная Салт.
                      </label>
                      <div class="w-full">    
                        <MultipleSelect 
                          @selectClose="search"
                          :dbValueKey="severnayaSaltovkaMicroDistrictsBaseVariables.dbValueKey"
                          :fieldChoiceText="severnayaSaltovkaMicroDistrictsBaseVariables.choiceText" 
                          :dictKey="severnayaSaltovkaMicroDistrictsBaseVariables.dictKey" 
                          :apiAddress="severnayaSaltovkaMicroDistrictsBaseVariables.fullApiAddress" 
                          :sendParamName="severnayaSaltovkaMicroDistrictsBaseVariables.sendParamName"
                          :addAction="addFindParam"
                          :removeAction="removeFindParam"
                          :removeKeyAction="removeFindParamKey"
                          placeholder="Микрорайоны" 
                        />
                      </div>
                    </div>
                  </TransitionDownRide>
                </div>
              </div>
            </TransitionDownRide>
            <div class="flex flex-wrap -mx-3 ">
              <div class="w-full md:w-2/4 px-3 pt-3 md:pt-6">
                <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Улицы
                </label>
                <div name="field" class="w-full">
                  <MultipleSelect 
                  @selectClose="search"
                  :dbValueKey="streetsBaseVariables.dbValueKey"
                  :fieldChoiceText="streetsBaseVariables.choiceText" 
                  :dictKey="streetsBaseVariables.dictKey" 
                  :apiAddress="streetsBaseVariables.fullApiAddress" 
                  :sendParamName="streetsBaseVariables.sendParamName"
                  :addAction="addFindParam"
                  :removeAction="removeFindParam"
                  :removeKeyAction="removeFindParamKey"
                  placeholder="Сумская, Пушкинская..." 
                  />
                </div>
              </div>
              <div class="w-full md:w-1/4 px-3 pt-3 md:pt-6">
                <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Номера домов
                </label>
                <div class="w-full">    
                  <MultipleTaggingSelect
                    @tagsChange="search"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    :sendParamName="houseNumberSendParamName"
                    :removeKeyAction="removeFindParamKey"
                    tagPlaceHolder="enter чтобы добавить к поиску"
                    placeholder="№"
                  />
                </div>
              </div>
               <div class="w-full md:w-1/4 px-3 pt-3 md:pt-6">
                <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Класс
                </label>
                <div name="field" class="w-full">
                    <MultipleSelect 
                    @selectClose="search"
                    :dbValueKey="theClassBaseVariables.dbValueKey"
                    :fieldChoiceText="theClassBaseVariables.choiceText" 
                    :dictKey="theClassBaseVariables.dictKey" 
                    :apiAddress="theClassBaseVariables.fullApiAddress" 
                    :sendParamName="theClassBaseVariables.sendParamName"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    :removeKeyAction="removeFindParamKey"
                    placeholder="Эконом, комфорт..." 
                    />
                  </div>
              </div>
            </div>
            <div class="flex flex-wrap -mx-3 ">
              <div class="w-full md:w-2/6 lg:2/5 px-3 pt-3 md:pt-6">
                <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Метро
                </label>
                <div name="field" class="w-full">
                  <MultipleSelect 
                  @selectClose="search"
                  :dbValueKey="metroBaseVariables.dbValueKey"
                  :fieldChoiceText="metroBaseVariables.choiceText" 
                  :dictKey="metroBaseVariables.dictKey" 
                  :apiAddress="metroBaseVariables.fullApiAddress" 
                  :sendParamName="metroBaseVariables.sendParamName"
                  :extraInformationField="metroBaseVariables.extraInformationText"
                  :addAction="addFindParam"
                  :removeAction="removeFindParam"
                  :removeKeyAction="removeFindParamKey"
                  placeholder="Университет, Олексеевская..." 
                  />
                </div>
              </div>
              <div class="w-full md:w-2/6 lg:1/5 px-3 pt-3 md:pt-6">
                <label class="block text-xs md:text-sm lg:text-base  font-bold text-gray-500  md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Время от метро
                </label>
                <div class="w-full">    
                  <div class="grid grid-cols-8 justify-center items-center">
                    <div class="col-span-1 text-xs md:text-sm lg:text-base">
                      До
                    </div>
                    <div class="col-span-5">
                      <vInputSearch
                        @valueChanged="search"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="timeFromMetroBaseVariables.sendParamName"
                        :removeKeyAction="removeFindParamKey"
                      />
                    </div>
                    <!-- <div class="hidden text-xs lg:text-base lg:block col-span-2">
                      Минут
                    </div> -->
                    <div class="text-xs md:text-sm lg:text-base col-span-2">
                      мин.
                    </div>
                  </div>
                </div>
              </div>
              <div class="w-full md:w-2/6 lg:2/5 px-3 pt-3 md:pt-6">
                <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Застройщики
                </label>
                <div name="field" class="w-full">
                  <MultipleSelect 
                    @selectClose="search"
                    :dbValueKey="developersBaseVariables.dbValueKey"
                    :fieldChoiceText="developersBaseVariables.choiceText" 
                    :dictKey="developersBaseVariables.dictKey" 
                    :apiAddress="developersBaseVariables.fullApiAddress" 
                    :sendParamName="developersBaseVariables.sendParamName"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    :removeKeyAction="removeFindParamKey"
                    placeholder="застройщики" 
                  />
                </div>
              </div>
            </div>
            <div class="flex w-full">
              <div class="m-auto w-3/5 pt-6 border-b-2 border-myHeaderColor opacity-25"></div>
            </div>
            <div class="flex pt-3 pb-4">
              <div class="w-1/3">
                Только в продаже
              </div>
              <div class="w-1/3 justify-center">
                <div class="text-gray-500 font-bold" :class="{'text-myMint-300' : isExtendedSearchActivated}">
                    Расширенный поиск
                </div>
                <div>
                  <toggle-button v-model="isExtendedSearchActivated" color="#00A480"/>
                </div>
              </div>
              <div class="w-1/3">
                  <p class="text-gray-500 font-bold">Что ищем?</p> 
                  <div class=''>
                    <span @click="updateShowFlatsOnly(false)" class="px-2 transition duration-300 cursor-pointer" :class="{'border-b-2 border-myMint-400 font-bold text-myMint-400':!showFlatsOnly}">Новострои</span> 
                    <span @click="updateShowFlatsOnly(true)" class="px-2 transition duration-300 cursor-pointer " :class="{'border-b-2 border-myMint-400 font-bold text-myMint-400':showFlatsOnly}">Квартиры в них</span>
                  </div>
              </div>
            </div>
            <div >
            <!-- <ExtendedSearchTransition> -->
              <div v-show="isExtendedSearchActivated">
                <div class="flex flex-wrap -mx-3 mb-3 md:mb-6">
                  <!-- <div class="w-full md:w-1/2 px-3 mb-3 md:mb-0">
                    <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                      Фильтр по застройщикам
                    </label>
                    <div name="field" class="w-full">
                      <MultipleSelect 
                      @selectClose="search"
                      :dbValueKey="developersBaseVariables.dbValueKey"
                      :fieldChoiceText="developersBaseVariables.choiceText" 
                      :dictKey="developersBaseVariables.dictKey" 
                      :apiAddress="developersBaseVariables.fullApiAddress" 
                      :sendParamName="developersBaseVariables.sendParamName"
                      :addAction="addFindParam"
                      :removeAction="removeFindParam"
                      :removeKeyAction="removeFindParamKey"
                      placeholder="застройщики" 
                      />
                    </div>
                  </div> -->
                  <div class="w-full md:w-1/2 px-3">
                    <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                      Введите номера домов на выбранных улицах
                    </label>
                    <div class="w-full">    
                      <MultipleTaggingSelect
                        @tagsChange="search"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="houseNumberSendParamName"
                        :removeKeyAction="removeFindParamKey"
                        tagPlaceHolder="enter чтобы добавить к поиску"
                        placeholder="Номера домов"
                      />
                    </div>
                  </div>
                </div>
              </div>
            <!-- </ExtendedSearchTransition> -->
            </div>
          </div>
          <!-- <button v-on:click="search" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
            п о и с к
          </button> -->
        </div>
     </div> 
    </div>
  <!-- </div> -->
</template>

<script>
import MultipleSelect from './v-multiple-select';
import MultipleTaggingSelect from './v-multiple-tagging-select';
import { 
  saltovkaDBKey,
  severnayaSaltovkaDBKey,
  houseNumberSendParamName,
  streetsBaseVariables,
  districtsBaseVariables,
  administrativeDistrictsBaseVariables,
  saltovkaMicroDistrictsBaseVariables,
  severnayaSaltovkaMicroDistrictsBaseVariables,
  developersBaseVariables,
  metroBaseVariables,
  theClassBaseVariables,
  timeFromMetroBaseVariables } from '../variables.js';
import { mapMutations, mapActions, mapGetters } from 'vuex'
import HomeSearchIcon from 'vue-material-design-icons/HomeSearch';
import GoogleMapsIcon from 'vue-material-design-icons/GoogleMaps';
import { addHashToLocation } from '../utils.js'
import TransitionDownRide from '../transitions/downRide'
import { ToggleButton } from 'vue-js-toggle-button'
// import ExtendedSearchTransition from '../transitions/extendedSearch'
// import searchComponentTransition from '../transitions/searchComponent'\
import smoothHeight from 'vue-smooth-height';
import vInputSearch from './v-input-search' ;

export default{
    components: {
        MultipleSelect,
        MultipleTaggingSelect,
        HomeSearchIcon,
        TransitionDownRide,
        ToggleButton,
        vInputSearch,
        GoogleMapsIcon
        // ExtendedSearchTransition,
        // searchComponentTransition
    },
    // В data только импортированные константные переменные
    data(){
      return{
        saltovkaDBKey:saltovkaDBKey,
        severnayaSaltovkaDBKey:severnayaSaltovkaDBKey,
        houseNumberSendParamName:houseNumberSendParamName,
        streetsBaseVariables:streetsBaseVariables,
        districtsBaseVariables:districtsBaseVariables,
        administrativeDistrictsBaseVariables:administrativeDistrictsBaseVariables,
        saltovkaMicroDistrictsBaseVariables:saltovkaMicroDistrictsBaseVariables,
        severnayaSaltovkaMicroDistrictsBaseVariables:severnayaSaltovkaMicroDistrictsBaseVariables,
        developersBaseVariables:developersBaseVariables,
        metroBaseVariables: metroBaseVariables,
        theClassBaseVariables: theClassBaseVariables,
        timeFromMetroBaseVariables: timeFromMetroBaseVariables,
        dataReady: false,
        isExtendedSearchActivated: false,
      }
   },
    // computed: {
    //     allBuildings(){
    //         console.log(this.$store.getters.allBuildings)
    //         return this.$store.getters.allBuildings;
    //     }
    // },
    // computed: {
    //     ...mapGetters(['allBuildings','buildingsCount'])
    //     },
    watch:{
      $route:"updateBuildings"
    },
    // beforeRouteUpdate(){
    //   this.updateBuildings()
    // },
    // created () {
    //    this.setInitialData()
    //  },
    methods:{ 
      ...mapMutations([
        // 'removeStreet',
        // 'addStreet'
        'addFindParam',
        'removeFindParam',
        'updateFindParams',
        'removeFindParamKey',
        'updateShowFlatsOnly'
      ]),
      ...mapActions([
        'searchBuildings',
        'checkToShowMicroDistricts',
        'checkToHideMicroDistricts',
        'setDefaultDistrictsChoosen',
        'searchFlats'
        // 'addStreet',
        // 'removeStreet',
        ]),
        search(){
          // alert('se')
          // alert(this.activeFindParams)
          // console.log('\tSEARCH')
          // alert(findParams)
          // const qs = require('qs')
          // this.searchBuildings(findParams)
          // console.log('ACTIVE FIND PARAMS BEFORE ROUTER REPLACE')
          // console.log(this.activeFindParams)
          
          // const template = {distict:["2",1]}
          // this.$store.dispatch('updateFindParams')
          // .then(() => 
          // this.$router.replace({name: 'search-page', query:this.activeFindParams})
          if(this.$route.path == '/'){
            this.removeFindParamKey('page')
            this.$router.replace({name:'search-buildings', query:this.activeFindParams})
          }
          else{
            // this.addHashToLocation(this.activeFindParams)
            this.removeFindParamKey('page')
            this.callAddHashToLocation()
            this.updateBuildings()
          }
          // this.$router.replace({name:'search-page', query:})
          // this.$router.replace({name: 'search-page', query:template})
        }, 
        visualSearchButtonTrigger(){
            // this.$refs.searchButton.classList.add("rotate-90");
            this.$refs.searchButton.classList.add("translate-y-1");
            this.$refs.searchButton.classList.add("text-myMint-300");
            setTimeout(() =>{
                // this.$refs.searchButton.classList.remove("rotate-90");
                this.$refs.searchButton.classList.remove("translate-y-1");
                this.$refs.searchButton.classList.remove("text-myMint-300");
            }, 400);
        },
        updateBuildings(){
          // if('page' in this.activeFindParams){
          //   alert()
          //   this.removeFindParamKey('page')
          // }
          if(this.showFlatsOnly){
            this.searchFlats(this.activeFindParams)
          }
          else{
            this.searchBuildings(this.activeFindParams)
          }
          this.visualSearchButtonTrigger()
        },
        callAddHashToLocation() {
          addHashToLocation(this.activeFindParams, this.$route.path)
        }
        // addHashToLocation(paramsDict) {
        //   console.log('aaaaaaaaaaaaaaaaa')
        //   console.log(this.$router)
        //   const qs = require('qs');
        //   const q = qs.stringify(paramsDict, {arrayFormat: 'repeat'})
        //   if(q.length > 0){
        //     history.replaceState(
        //       {},
        //       null,
        //       '#' + this.$route.path + '?' + q
        //       )
        //   }
        //   else{
        //     history.pushState(
        //       {},
        //       null,
        //       '#' + this.$route.path,
        //       )
        //   }
        // }
        // setInitialData(){
        //   this.updateFindParams(JSON.parse(JSON.stringify(this.$route.query)))
        // },
        // async prepareData(){
        //   await this.updateBuildings()
        // }
    },
    // created() {
    //   this.setInitialData()
    // },
    // mounted(){
    //   this.prepareData()
    //         .then(() => {
    //             this.changeLoadingState(true)
    //             }
    //         )   
    // },
    computed: {
      ...mapGetters([
        'activeFindParams', 
        'isSaltovkaDistrictChoosen', 
        'isSevernayaSaltovkaDistrictChoosen',

        'selectedStreets',
        'selectedDistricts',
        'selectedAdministrativeDistricts',
        'selectedHouseNumbers',
        'selectedDevelopers',
        'selectedSaltovkaMicroDistricts',
        'selectedSevernayaSaltovkaMicroDistricts',
        'showFlatsOnly'
        ])
    },
    mounted(){
      // if('' in this.activeFindParams){
      //   this.isExtendedSearchActivated = true
      // }
      this.$smoothElement({
            el: this.$refs.searchComponent,
            hideOverflow: true
        })
    },
    mixins:[
       smoothHeight
       ],

}

</script>


<style scoped>

/* div { */
 
  /* transition:max-height 0.3s ease-out; 
  max-height:auto; */
/* } */
/* #searchComponent.collapsed {
  max-height: 0;
} */

</style>
