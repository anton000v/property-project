<template>
  <div>
    <section class="pb-20 bg-gray-300 -mt-32">
      <!-- <div> -->
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
                    <i class="fas fa-retweet"></i>
                  </div>
                  <div class="flex flex-wrap -mx-3 mb-6">
                    <div class="w-full md:w-1/2 md:flex md:items-center px-3 mb-6 md:mb-0">
                      <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="inline-full-name">
                        Улицы
                      </label>
                      <div name="field" class="w-full">
                        <MultipleSelect 
                        @update = "updateBuildings" 
                        :searchKey="streetsSearchKey"
                        :fieldChoiceText="streetsChoiceText" 
                        :dictKey="streetsDictKey" 
                        :apiAddress="getStreetsApiAddress" 
                        placeholder="Улицы" 
                        />
                      </div>
                    </div>
                    <!-- <div class="w-full md:w-1/2 md:flex md:items-center px-3 mb-6 md:mb-0">
                      <div class="w-full md:w-full md:flex md:items-center px-3 mb-6 md:mb-0">
                        <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="inline-full-name">
                          Дом
                        </label>
                        <div class="w-full">
                         
                        <MultipleTaggingSelect
   
                        />
                        </div>
                      </div>
                    </div> -->
                  </div>
                  <div class="flex flex-wrap -mx-3 mb-6">
                  <div class="w-full md:w-full md:flex md:items-center px-3 mb-6 md:mb-0">
                      <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                        Административные районы
                      </label>
                        <div name="field" class="w-full">
                          <MultipleSelect 
                          @update = "updateBuildings" 
                          :searchKey="administrativeDistrictsSearchKey"
                          :fieldChoiceText="administrativeDistrictsChoiceText" 
                          :dictKey="administrativeDistrictsDictKey" 
                          :apiAddress="getAdministrativeDistrictsApiAddress" 
                          placeholder="Административные районы" 
                          />
                      </div>
                    </div>
                  </div>
                  <div class="flex flex-wrap -mx-3 mb-6">
                    <div class="w-full md:w-full md:flex md:items-center px-3 mb-6 md:mb-0">
                      <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="inline-full-name">
                        Районы
                      </label>
                      <div class="w-full">
                        <div name="field" class="w-full">
                          <MultipleSelect 
                          @update = "updateBuildings" 
                          :searchKey="districtsSearchKey"
                          :extraInformationField="districtExtraInformation"
                          :fieldChoiceText="districtChoiceText" 
                          :dictKey="districtDictKey" 
                          :apiAddress="getDistrictsApiAddress" 
                          placeholder="Районы" 
                          />
                        </div>
                      </div>
                    </div>
                    <!-- <div class="w-full md:w-1/2 md:flex md:items-center px-3 mb-6 md:mb-0">
                      <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                        Микрорайон
                      </label>
                      <div name="field" class="w-full"> 
                        <MultipleSelect 
                          :fieldChoiceText="microDistrictChoiceText" 
                          :dictKey="microDistrictDictKey" 
                          :apiAddress="getMicroDistrictsApiAddress" 
                          :nestedKeys="microDistrictNestedKeys"
                          placeholder="Микрорайоны" 
                        />
                      </div>
                    </div> -->
                  </div>
                  <!-- <div class="flex flex-wrap -mx-3 mb-6" v-if="isSaltovkaChoices">
                    <div class="w-full md:w-1/2 md:flex md:items-center px-3 mb-6 md:mb-0">
                      <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="inline-full-name">
                        Микрорайоны Салтовки
                      </label>
                      <div class="w-full">
                        <div name="field" class="w-full">
                          <MultipleSelect 
                          v-model = "district" 
                          :extraInformationField="districtExtraInformation"
                          :fieldChoiceText="districtChoiceText" 
                          :dictKey="districtDictKey" 
                          :apiAddress="getDistrictsApiAddress" 
                          placedictkholder="Районы" 
                          />
                        </div>
                      </div>
                    </div>
                    <div class="w-full md:w-1/2 md:flex md:items-center px-3 mb-6 md:mb-0">
                      <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                        Микрорайоны Северной Салтовки
                      </label>
                      <div name="field" class="w-full"> 
                        <MultipleSelect 
                          :fieldChoiceText="microDistrictChoiceText" 
                          :dictKey="microDistrictDictKey" 
                          :apiAddress="getMicroDistrictsApiAddress" 
                          :nestedKeys="microDistrictNestedKeys"
                          placeholder="Микрорайоны" 
                        />
                      </div>
                    </div>
                  </div> -->
                </div>
                <button v-on:click="updateBuildings" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
                  п о и с к
                </button>
              </div>
            </div>
          </div>

            <div v-if="Object.keys(allBuildingsList.buildings).length > 0" class="grid m-auto sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 justify-center gap-4 my-20">
              <PropertyCard v-for="building in allBuildingsList.buildings" :key="building.slug" :building="building"/>    
            </div>          
            <div v-else class="grid justify-center"> 
              <h2>По вашему запросу ничего не найдено :с</h2>
            </div>



                <!-- <section v-if="errored">
          <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
        </section>

        <section v-else>
          <div v-if="loading">Loading...</div>

          <div
            v-else
            v-for="currency in info"
            class="currency"
          >
            {{ currency.description }}:
            <span class="lighten">
              <span v-html="currency.symbol"></span>{{ currency.rate_float | currencydecimal }}
            </span>
          </div>

        </section> -->
         
       
        </div> <!-- Container end! -->
    </section>
  </div>
</template>

<script>
// import TodoList from './TodoList.vue';
// import Testapi from './testapi.vue';
// import Button from './button.vue';
import MultipleSelect from './multipleSelect';
// import MultipleTaggingSelect from './multipleTaggingSelect';
import PropertyCard from './PropertyCard.vue';
import { baseApiAddress } from '../variables.js';
// import Property from './PropertyCard.vue';

export default{
  props: ['Body'],
  data(){
    return {
      // district:'',
      // todos: ['Ремонт', 'Something else', 'lalala'],
      // microDistrictsChoices: null,
      allBuildingsList: null,

      getStreetsApiAddress:"get-streets/" ,
      streetsDictKey:'streets',
      streetsChoiceText:'street_ru',
      streetsSearchKey:'id',

      getDistrictsApiAddress:"get-districts/",
      districtDictKey:'districts',
      districtChoiceText:'text_value',
      districtExtraInformation:'direction',
      districtsSearchKey:'db_value',

      getAdministrativeDistrictsApiAddress:"get-administrative-districts/",
      administrativeDistrictsDictKey:'administrative_districts',
      administrativeDistrictsChoiceText:'administrative_dist_ru',
      administrativeDistrictsSearchKey:'id',

      isSaltovkaChoices:false,
      isSevernayaSaltovkaChoices:false,

      streets:null,
      districts: null,
      administrativeDistricts:null,

      searchBuildingUrl: 'find-buildings/'
      // getMicroDistrictsApiAddress:"get-micro-districts/",
      // microDistrictDictKey:'micro_districts',
      // microDistrictNestedKeys:['not_divided'],
      // microDistrictChoiceText:'text_value',
    }
  },
  components: {
    // Testapi,
    // Button,
    MultipleSelect,
    PropertyCard,
    // MultipleTaggingSelect,
  },
  mounted() {
    const axios = require('axios');
      axios.get(baseApiAddress + 'get-micro-districts/').then(resp => {
          this.microDistrictsChoices = resp.data.micro_district_choices;
      });
      axios.get(baseApiAddress + 'find-buildings/').then(resp => {
          this.allBuildingsList = resp.data;
      })
      // axios.get(baseApiAddress + 'find-buildings/').then(resp => {
      //     this.allBuildingsList = resp.data;
      // })
  },
  // watch: {
    // эта функция запускается при любом изменении района
    // district: function (value) {
      // alert(value)
      // console.log(value)
      // ------------- Проверка салтовка северная салтовка
      // this.isSaltovkaChoices = false
      // this.isSevernayaSaltovkaChoices = false
      // value.forEach(function(item) {
      //   // Проверка, есть ли в массиве районов Салтовка
      //    if (item.db_value == 'sal'){ 
      //     //  alert('Салтовка!')
      //      this.isSaltovkaChoices = true
      //    }
      //    // Проверка, есть ли в массиве районов Северная Салтовка
      //    else if(item.db_value == 'ses'){
      //     //  alert('Северная Салтовка!')
      //     this.isSevernayaSaltovkaChoices = true
      //    }
      // });
    // }
  // },
  methods: {
    // deleteTodo(index){
    //   this.todos.splice(index, 1);
    // checkAndLoad: function(text) {
    //   // `this` внутри методов указывает на экземпляр Vue
    //   alert(text);
    //   }
      updateSearchValues(dictk, value){
        switch (dictk){
          case this.streetsDictKey:
            this.streets = value
            break

          case this.districtDictKey:
            this.districts = value
            break

          case this.administrativeDistrictsDictKey:
            this.administrativeDistricts = value
            break
        }
      },
      updateBuildings(dictk, value){
        this.updateSearchValues(dictk, value)
        const axios = require('axios');

      // axios.get(baseApiAddress + 'find-buildings/').then(resp => {
      //     this.allBuildingsList = resp.data;
      // })
        const findParams = {}
        if(this.streets){
          findParams['street'] = this.streets
        }
        if(this.districts){
          findParams['district'] = this.districts
        }
        if(this.administrativeDistricts){
          findParams['administrative_district'] = this.administrativeDistricts
        }
        // findParams[1] = 2
        console.log(findParams)
        const qs = require('qs');
        axios.get(baseApiAddress + this.searchBuildingUrl, {
          params: findParams,
          paramsSerializer: params => {
            console.log(' PARAMS: ')
            console.log(qs.stringify(params, {arrayFormat: 'repeat'}))  
            return qs.stringify(params, {arrayFormat: 'repeat'})
          }
          }).then(resp => {
          this.allBuildingsList = resp.data;
        })
      },

    }
}
</script>
change