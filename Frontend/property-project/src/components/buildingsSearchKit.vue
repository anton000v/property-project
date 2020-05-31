<template>

  <div class="container mx-auto px-8">
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
                  @selectClose="searchBuildings(activeFindParams)"
                  :dbValueKey="administrativeDistrictsBaseVariables.dbValueKey"
                  :fieldChoiceText="administrativeDistrictsBaseVariables.choiceText" 
                  :dictKey="administrativeDistrictsBaseVariables.dictKey" 
                  :apiAddress="administrativeDistrictsBaseVariables.fullApiAddress" 
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
                    @selectClose="searchBuildings(activeFindParams)" 
                    @select="checkToShowMicroDistricts"
                    @remove="checkToHideMicroDistricts"
                    :dbValueKey="districtsBaseVariables.dbValueKey"
                    :extraInformationField="districtsBaseVariables.extraInformationText"
                    :fieldChoiceText="districtsBaseVariables.choiceText" 
                    :dictKey="districtsBaseVariables.dictKey" 
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
                    @selectClose="searchBuildings(activeFindParams)"
                    :dbValueKey="saltovkaMicroDistrictsBaseVariables.dbValueKey"
                    :fieldChoiceText="saltovkaMicroDistrictsBaseVariables.choiceText" 
                    :dictKey="saltovkaMicroDistrictsBaseVariables.dictKey" 
                    :apiAddress="saltovkaMicroDistrictsBaseVariables.fullApiAddress" 
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
                      @selectClose="searchBuildings(activeFindParams)"
                      :dbValueKey="severnayaSaltovkaMicroDistrictsBaseVariables.dbValueKey"
                      :fieldChoiceText="severnayaSaltovkaMicroDistrictsBaseVariables.fieldChoiceText" 
                      :dictKey="severnayaSaltovkaMicroDistrictsBaseVariables.dictKey" 
                      :apiAddress="severnayaSaltovkaMicroDistrictsBaseVariables.fullApiAddress" 
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
                  @selectClose="searchBuildings(activeFindParams)"
                  :dbValueKey="streetsBaseVariables.dbValueKey"
                  :fieldChoiceText="streetsBaseVariables.choiceText" 
                  :dictKey="streetsBaseVariables.dictKey" 
                  :apiAddress="streetsBaseVariables.fullApiAddress" 
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
                    @tagsChange="searchBuildings(activeFindParams)"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    :searchKey="houseNumberSearchKey"
                    tagPlaceHolder="enter чтобы добавить к поиску"
                    placeholder="Номера домов"
                  />
                </div>
              </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
              <!-- <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                  Фильтр по застройщикам
                </label>
                <div name="field" class="w-full">
                  <MultipleSelect 
                  @selectClose="searchBuildings(activeFindParams)"
                  :searchKey="developersSearchKey"
                  :fieldChoiceText="developersChoiceText" 
                  :dictKey="developersDictKey" 
                  :apiAddress="getDevelopersApiAddress" 
                  placeholder="застройщики" 
                  />
                </div>
              </div> -->
            </div>
          </div>
          <button v-on:click="searchBuildings" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
            п о и с к
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MultipleSelect from './multipleSelect';
import MultipleTaggingSelect from './multipleTaggingSelect';
import { 
  saltovkaDBKey,
  severnayaSaltovkaDBKey,
  houseNumberSearchKey,
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
        houseNumberSearchKey:houseNumberSearchKey,
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
    methods:{ 
      ...mapMutations([
        // 'removeStreet',
        // 'addStreet'
        'addFindParam',
        'removeFindParam'
      ]),
      ...mapActions([
        'searchBuildings', 
        'checkToShowMicroDistricts',
        'checkToHideMicroDistricts',
        // 'addStreet',
        // 'removeStreet',
        ])
    },
    async mounted() {
      this.searchBuildings();
    },
    computed: {
      ...mapGetters([
        'activeFindParams', 
        'isSaltovkaDistrictChoosen', 
        'isSevernayaSaltovkaDistrictChoosen',
        ])
    },
}

</script>