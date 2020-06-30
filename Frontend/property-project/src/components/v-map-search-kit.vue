<template>
    <div>
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
                                        <GoogleMapsIcon title="Принудительный поиск"/>
                                        </div>
                                    </div>
                                <!-- <div class="m-auto bg-myHeaderColor text-white p-1 -ml-2 rounded-r-lg">
                                    По карте
                                </div> -->
                                <!-- </div> -->
                            </div>
                            <div class="w-full md:w-1/3">
                                <p class="-my-4 text-sm">Надоела карта? Можете выбрать</p>
                                <!-- <p class="text-xs block md:hidden">Можете выбрать</p> -->
                                <router-link :to="{name:'search-buildings'}">
                                <div  class="my-4 h-full group bg-myHeaderColor flex rounded-lg cursor-pointer transition duration-500 transform hover:translate-y-1 hover:shadow-xl">
                                    <div class="m-auto">
                                    <div class="flex"> 
                                        <HomeSearchIcon class="m-auto text-white transition duration-500 group-hover:text-myMint-300"/>
                                        <p class="text-white pl-2 text-base p-2">Обычный поиск</p>
                                    </div>
                                    </div>
                                </div>
                                </router-link>
                            </div>
                        </div>
                        <div class="flex flex-wrap -mx-3  overflow-visible">
                            <div class="w-full md:w-1/2 px-3 pt-3 md:pt-6">
                                <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
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
                            <div class="w-full md:w-1/2 lg:2/5 px-3 pt-3 md:pt-6">
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
                    </div>
                    <div class="px-4 py-5 flex-auto" ref='searchComponent' >
                        <div class="flex flex-wrap -mx-3  overflow-visible">
                            <div class="w-full md:w-2/3 lg:2/5 px-3 ">
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
                                placeholder="Станция" 
                                />
                                </div>
                            </div>
                            <div class="w-full md:w-1/3 lg:1/5 px-3 ">
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
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import MultipleSelect from './v-multiple-select';
import { 
  developersBaseVariables,
  metroBaseVariables,
  theClassBaseVariables,
  timeFromMetroBaseVariables } from '../variables.js';
import { mapMutations, mapActions, mapGetters } from 'vuex'
import { addHashToLocation } from '../utils.js'
import vInputSearch from './v-input-search' ;
import HomeSearchIcon from 'vue-material-design-icons/HomeSearch';
import GoogleMapsIcon from 'vue-material-design-icons/GoogleMaps';
export default {
    components:{
        MultipleSelect,
        vInputSearch,
        HomeSearchIcon,
        GoogleMapsIcon
    },
    data(){
        return{
            developersBaseVariables:developersBaseVariables,
            metroBaseVariables: metroBaseVariables,
            theClassBaseVariables: theClassBaseVariables,
            timeFromMetroBaseVariables: timeFromMetroBaseVariables,
        }
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
   
    watch:{
      $route:"updateBuildings"
    },
    methods:{ 
      ...mapMutations([

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

        ]),
        search(){
          if(this.$route.path == '/'){
            this.removeFindParamKey('page')
            this.$router.replace({name:'search-buildings', query:this.activeFindParams})
          }
          else{
            this.removeFindParamKey('page')
            this.callAddHashToLocation()
            this.updateBuildings()
          }
        }, 
        updateBuildings(){
          this.searchBuildings(this.activeFindParams)
            // this.$refs.searchButton.mouseover()
            this.visualSearchButtonTrigger()
        },
        callAddHashToLocation() {
          addHashToLocation(this.activeFindParams, this.$route.path)
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
        }
        
    },
    mounted(){
    //   if('' in this.activeFindParams){
    //     this.isExtendedSearchActivated = true
    //   }
    //   this.$smoothElement({
    //         el: this.$refs.searchComponent,
    //         hideOverflow: true
    //     })
    },
}
</script>