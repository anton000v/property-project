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
                    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                      <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                        Выберите административные районы
                      </label>
                      <div name="field" class="w-full">
                        <MultipleSelect 
                        @selectClose = "updateBuildings" 
                        :searchKey="administrativeDistrictsSearchKey"
                        :fieldChoiceText="administrativeDistrictsChoiceText" 
                        :dictKey="administrativeDistrictsDictKey" 
                        :apiAddress="getAdministrativeDistrictsApiAddress" 
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
                          @selectClose = "updateBuildings" 
                          @select = "checkToShowMicroDistricts"
                          @remove = "checkToHideMicroDistricts"
                          :searchKey="districtsSearchKey"
                          :extraInformationField="districtExtraInformation"
                          :fieldChoiceText="districtChoiceText" 
                          :dictKey="districtDictKey" 
                          :apiAddress="getDistrictsApiAddress" 
                          :trackEveryUpdate="true"
                          placeholder="Районы" 
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                   <div class="flex flex-wrap -mx-3 mb-6" v-if="isSaltovkaDistrictChoosen || isSevernayaSaltovkaDistrictChoosen">
                    <div class='w-1/2'></div>
                    <div class="w-full md:w-1/2 flex" >  
                      <!-- Выберите микрорайоны -->
                      <!-- <div class='w-full flex'> -->
                        <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0 " v-if="isSaltovkaDistrictChoosen">
                          <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                            Салтовка
                          </label>
                          <div name="field" class="w-full">
                            <MultipleSelect 
                            @selectClose = "updateBuildings" 
                            :searchKey="microDistrictsSearchKey"
                            :fieldChoiceText="microDistrictsChoiceText" 
                            :dictKey="saltovkaMicroDistrictsDictKey" 
                            :apiAddress="getSaltovkaMicroDistrictsApiAddress" 
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
                              @selectClose = "updateBuildings" 
                              :searchKey="microDistrictsSearchKey"
                              :fieldChoiceText="microDistrictsChoiceText" 
                              :dictKey="severnayaSaltovkaMicroDistrictsDictKey" 
                              :apiAddress="getSevernayaSaltovkaMicroDistrictsApiAddress" 
                              placeholder="Микрорайоны" 
                            />
                          </div>
                        <!-- </div> -->
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
                        @selectClose = "updateBuildings" 
                        :searchKey="streetsSearchKey"
                        :fieldChoiceText="streetsChoiceText" 
                        :dictKey="streetsDictKey" 
                        :apiAddress="getStreetsApiAddress" 
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
                          @selectClose = "updateBuildings" 
                          :searchKey="houseNumberSearchKey"
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
                        @selectClose = "updateBuildings" 
                        :searchKey="streetsSearchKey"
                        :fieldChoiceText="streetsChoiceText" 
                        :dictKey="streetsDictKey" 
                        :apiAddress="getStreetsApiAddress" 
                        placeholder="застройщики" 
                        />
                      </div>
                    </div>
                    <!-- <div class="w-full md:w-1/2 px-3">
                      <label class="block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                        Введите номера домов на выбранных улицах
                      </label>
                      <div class="w-full">    
                        <MultipleTaggingSelect
                          @selectClose = "updateBuildings" 
                          :searchKey="houseNumberSearchKey"
                          tagPlaceHolder="enter чтобы добавить к поиску"
                          placeholder="Номера домов"
                        />
                      </div>
                    </div> -->
                  </div>
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
        </section>selectedValue

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
import MultipleTaggingSelect from './multipleTaggingSelect';
import PropertyCard from './PropertyCard.vue';
import { baseApiAddress } from '../variables.js';

export default{
  data(){
    return {
      allBuildingsList: null,

      saltovkaDBValue: null,
      severnayaSaltovkaDBValue: null,
      saltovkaDBKey:'saltovka_db_value',
      severnayaSaltovkaDBKey:'severnaya_saltovka_db_value',


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

      houseNumberSearchKey: 'house_number',

      isSaltovkaDistrictChoosen: false,
      isSevernayaSaltovkaDistrictChoosen: false,

      microDistrictsChoiceText: 'text_value',
      microDistrictsSearchKey: 'db_value',
      getSaltovkaMicroDistrictsApiAddress: 'get-saltovka-micro-districts/',
      saltovkaMicroDistrictsDictKey: 'saltovka_micro_districts',
      getSevernayaSaltovkaMicroDistrictsApiAddress: 'get-severnaya-saltovka-micro-districts/',
      severnayaSaltovkaMicroDistrictsDictKey: 'severnaya_saltovka_micro_districts',

      streets:null,
      districts: null,
      administrativeDistricts:null,
      houseNumbers:null,
      saltovkaMicroDistricts:null,
      severnayaSaltovkaMicroDistricts:null,

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
    MultipleTaggingSelect,
  },
  mounted() {
    const axios = require('axios');
      // axios.get(baseApiAddress + 'get-micro-districts/').then(resp => {
      //     this.microDistrictsChoices = resp.data.micro_district_choices;
      // })
      axios.get(baseApiAddress + 'find-buildings/').then(resp => {
          this.allBuildingsList = resp.data;
      })
      axios.get(baseApiAddress + 'get-saltovka-severnaya-saltovka-db-values/').then(resp => {
          this.saltovkaDBValue = resp.data[this.saltovkaDBKey];
          this.severnayaSaltovkaDBValue = resp.data[this.severnayaSaltovkaDBKey];
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

          case this.houseNumberSearchKey:
            this.houseNumbers = value
            break

          case this.saltovkaMicroDistrictsDictKey:
            this.saltovkaMicroDistricts = value
            break
          case this.severnayaSaltovkaMicroDistrictsDictKey:
            this.severnayaSaltovkaMicroDistricts = value
        }
      },
      updateBuildings(dictk, value){
        this.updateSearchValues(dictk, value)
        const axios = require('axios');
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
        if(this.houseNumbers){
          findParams[this.houseNumberSearchKey] = this.houseNumbers
        }
        if(this.saltovkaMicroDistricts){
          findParams['saltovka_microdistrict'] = this.saltovkaMicroDistricts
        }
        if(this.severnayaSaltovkaMicroDistricts){
          findParams['severnaya_saltovka_microdistrict'] = this.severnayaSaltovkaMicroDistricts
        }
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
      // checkToShowSaltovkaMicroDistricts(value){
      //   if(value.includes('sal')){
      //     if(!this.isSaltovkaChoosen){
      //       alert('Салтовка выбрана!')
      //       this.isSaltovkaChoosen = true
      //     }
      //   }
      //   else{
      //     if(this.isSaltovkaChoosen){
      //       alert('Салтовка выключена!')
      //       this.isSaltovkaChoosen = false
      //     }
      //   }
      // },
      checkToShowMicroDistricts(selectedValue){
        if(selectedValue == this.saltovkaDBValue){
          if(!this.isSaltovkaDistrictChoosen){
            // alert('Салтовка выбрана!')
            this.isSaltovkaDistrictChoosen = true
          }
        }
        else if(selectedValue == this.severnayaSaltovkaDBValue){
          if(!this.isSevernayaSaltovkaDistrictChoosen){
            // alert('Северная салтовка выбрана!')
            this.isSevernayaSaltovkaDistrictChoosen = true
          }
        }
        // else{
        //   if(this.isSaltovkaDistrictChoosen){
        //     alert('Салтовка выключена!')
        //     this.isSaltovkaDistrictChoosen = false
        //   }
        //   if(this.isSevernayaSaltovkaDistrictChoosen){
        //     alert('Северная салтовка выключена')
        //     this.isSevernayaSaltovkaDistrictChoosen = false
        //   }
        // }
    },
    checkToHideMicroDistricts(removedValue){
        if(removedValue == this.saltovkaDBValue){
          if(this.isSaltovkaDistrictChoosen){
            // alert('Салтовка выключена!')
            this.isSaltovkaDistrictChoosen = false
          }
        }
        else if(removedValue == this.severnayaSaltovkaDBValue){
          if(this.isSevernayaSaltovkaDistrictChoosen){
            // alert('Северная салтовка выключена!')
            this.isSevernayaSaltovkaDistrictChoosen = false
          }
        }
    }
  }
}
</script>