<template>

  <!-- <div class="container mx-auto px-8"> -->
    <div class="flex flex-wrap">
      <div class="w-full text-center"> 
        <div
          class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
        >
          <div class="px-4 py-5 flex-auto">
            <div
              class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-blue-400"
            >
              <i class="fas fa-retweet">III</i>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
              <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Выберите административные районы
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
                  placeholder="Административные районы" 
                  />
                </div>
              </div>
              <div class="w-full md:w-1/2 px-3">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="inline-full-name">
                  Выберите районы
                </label>
                <div class="w-full">
                  <div name="field" class="w-full">
                    <MultipleSelect 
                    @selectClose="search" 
                    @select="checkToShowMicroDistricts"
                    @remove="checkToHideMicroDistricts"
                    :dbValueKey="districtsBaseVariables.dbValueKey"
                    :extraInformationField="districtsBaseVariables.extraInformationText"
                    :fieldChoiceText="districtsBaseVariables.choiceText" 
                    :dictKey="districtsBaseVariables.dictKey" 
                    :sendParamName="districtsBaseVariables.sendParamName"
                    :apiAddress="districtsBaseVariables.fullApiAddress" 
                    :trackEveryUpdate="true"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    placeholder="Районы" 
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6" v-if="isSaltovkaDistrictChoosen || isSevernayaSaltovkaDistrictChoosen">
              <div class='w-1/2'></div>
              <div class="w-full md:w-1/2 flex" >  
                <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0 " v-if="isSaltovkaDistrictChoosen">
                  <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
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
                    placeholder="Микрорайоны" 
                    />
                  </div>
                </div>
                <div class="w-full md:w-1/2 px-3" v-if="isSevernayaSaltovkaDistrictChoosen">
                  <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                    Северная салтовка
                  </label>
                  <div class="w-full">    
                    <MultipleSelect 
                      @selectClose="search"
                      :dbValueKey="severnayaSaltovkaMicroDistrictsBaseVariables.dbValueKey"
                      :fieldChoiceText="severnayaSaltovkaMicroDistrictsBaseVariables.fieldChoiceText" 
                      :dictKey="severnayaSaltovkaMicroDistrictsBaseVariables.dictKey" 
                      :apiAddress="severnayaSaltovkaMicroDistrictsBaseVariables.fullApiAddress" 
                      :sendParamName="severnayaSaltovkaMicroDistrictsBaseVariables.sendParamName"
                      :addAction="addFindParam"
                      :removeAction="removeFindParam"
                      placeholder="Микрорайоны" 
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
              <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Выберите улицы
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
                  placeholder="Улицы" 
                  />
                </div>
              </div>
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
                    tagPlaceHolder="enter чтобы добавить к поиску"
                    placeholder="Номера домов"
                  />
                </div>
              </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
              <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
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
                  placeholder="застройщики" 
                  />
                </div>
              </div>
            </div>
          </div>
          <button v-on:click="search" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
            п о и с к
          </button>
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
  developersBaseVariables } from '../variables.js';
import { mapMutations, mapActions, mapGetters } from 'vuex'

export default{
    components: {
        MultipleSelect,
        MultipleTaggingSelect,
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
    methods:{ 
      ...mapMutations([
        // 'removeStreet',
        // 'addStreet'
        'addFindParam',
        'removeFindParam',
        'updateFindParams',

      ]),
      ...mapActions([
        'searchBuildings',
        'checkToShowMicroDistricts',
        'checkToHideMicroDistricts',
        
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
          this.$router.replace({query:this.activeFindParams})
          // this.$router.replace({name:'search-page', query:})
          // this.$router.replace({name: 'search-page', query:template})
        }, 
        updateBuildings(){
          this.searchBuildings(this.activeFindParams)
        }
    },
    mounted(){
      // alert(this.$route.query)
      this.updateFindParams(JSON.parse(JSON.stringify(this.$route.query)))
      // console.log("  [from mounted]  Find param:")
      // console.log(this.activeFindParams)
      this.updateBuildings()
    },
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

}

</script>