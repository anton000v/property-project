<template>

    <!-- <div :if="dataReady"> -->
    <!-- <div id="searchComponent" :class="{'collapsed' : !isExtendedSearchActivated}" class="flex flex-wrap"> -->
    <div class="flex flex-wrap">
      <div class="w-full text-center"> 
        <div
          class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"  
        >
          <div class="px-4 py-5 flex-auto" ref='searchComponent' >
            <div class="inline-flex " >

              <div
                class="inline-block text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full transition duration-500 bg-myMint-300 hover:bg-myMint-100 cursor-pointer"
                v-on:click="search"
              >
                <HomeSearchIcon/>
              </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-3 md:mb-6" >
              <div class="w-full md:w-1/2 px-3 mb-3 md:mb-0">
                <label class="hidden md:block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Административные районы
                </label>
                <label class="block md:hidden text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
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
                  placeholder="Административные районы" 
                  />
                </div>
              </div>
              <div class="w-full md:w-1/2 px-3">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="inline-full-name">
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
                    placeholder="Районы" 
                    />
                  </div>
                </div>
              </div>
            </div>
            <TransitionDownRide>
              <div class="flex flex-wrap -mx-3 md-3 md:mb-6" v-if="isSaltovkaDistrictChoosen || isSevernayaSaltovkaDistrictChoosen">
                <div class='w-1/2'></div>
                <div class="w-full md:w-1/2 grid grid-cols-2" >  
                  <TransitionDownRide>
                    <div class="w-full px-3 mb-3 md:mb-0 " v-if="isSaltovkaDistrictChoosen">
                      <label class="block text-sm md:text-base text-gray-500 md:font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
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
                    <div class="w-full px-3" v-if="isSevernayaSaltovkaDistrictChoosen">
                      <label class="hidden md:block text-sm md:text-base text-gray-500 md:font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                        Северная Салтовка.
                      </label>
                      <label class="block md:hidden text-sm md:text-base text-gray-500 md:font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
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
            <div class="flex flex-wrap -mx-3 mb-3 md:mb-6">
              <div class="w-full md:w-2/4 px-3 mb-3 md:mb-0">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
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
                  placeholder="Улицы" 
                  />
                </div>
              </div>
              <div class="w-full md:w-1/4 px-3">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
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
                    placeholder="Номера домов"
                  />
                </div>
              </div>
               <div class="w-full md:w-1/4 px-3">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Классы
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
                    placeholder="Классы" 
                    />
                  </div>
              </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-3 md:mb-6">
              <div class="w-full md:w-2/5 px-3 mb-3 md:mb-0">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
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
                  placeholder="Станция" 
                  />
                </div>
              </div>
              <div class="w-full md:w-1/5 px-3">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Время от метро
                </label>
                <div class="w-full">    
                  <div class="grid grid-cols-5 justify-center items-center">
                    <div class="col-span-1">
                      До
                    </div>
                    <div class="col-span-2">
                      <vInputSearch
                        @valueChanged="search"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="timeFromMetroBaseVariables.sendParamName"
                        :removeKeyAction="removeFindParamKey"
                      />
                    </div>
                    <div class="col-span-2">
                      Минут
                    </div>
                  </div>
                </div>
              </div>
              <div class="w-full md:w-2/5 px-3 mb-3 md:mb-0">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
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

            <div class="pt-2 pb-2 justify-center">
              <div class="text-gray-500 font-bold" :class="{'text-myMint-300' : isExtendedSearchActivated}">
                  Расширенный поиск
              </div>
              <div>
                <toggle-button v-model="isExtendedSearchActivated" color="#00A480"/>
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
        vInputSearch
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
        isExtendedSearchActivated: false
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
      ]),
      ...mapActions([
        'searchBuildings',
        'checkToShowMicroDistricts',
        'checkToHideMicroDistricts',
        'setDefaultDistrictsChoosen'
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
            this.$router.replace({name:'search-page', query:this.activeFindParams})
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
        updateBuildings(){
          // if('page' in this.activeFindParams){
          //   alert()
          //   this.removeFindParamKey('page')
          // }
          this.searchBuildings(this.activeFindParams)
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
        ])
    },
    mounted(){
      if('' in this.activeFindParams){
        this.isExtendedSearchActivated = true
      }
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
