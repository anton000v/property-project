<template>
  <div> 
    <!-- {{ fieldChoiceText }} {{ searchKey }} {{ apiAddress }} {{ dictKey }} -->
    <!-- <p>{{ activeFindParams }}</p>
    <p>{{ value }}</p> -->
      <div class="flex items-center">
        <TransitionLeftRide>
          <div class='flex-1 px-1 cursor-pointer text-sm transition duration-500 ease-in-out  hover:opacity-40 transform hover:-translate-y-1 hover:-rotate-90 text-myMint-400 hover:text-myMint-100' v-show="showClearAllButton" @click="clearAll">
              <CloseCircleOutlineIcon :size="20"  title="Очистить все"/>
          </div>
        </TransitionLeftRide>
        <div class='w-full'>
            <multiselect 
              v-model="value" 
              @select="SelectValueAction"
              @close="SelectCloseAction"
              @remove="removeValueAction"
              :options="options" 
              :multiple="true" 
              :close-on-select="false" 
              :clear-on-select="false" 
              :preserve-search="true" 
              :placeholder="placeholder" 
              :label="fieldChoiceText"

              :track-by="fieldChoiceText" 
              :preselect-first="true" 
              
            

              selectLabel="выбрать" 
              deselectLabel="удалить" 
              selectedLabel="выбрано"
              >
              
                <template slot="selection" slot-scope="{ values, search, isOpen }"><span class="multiselect__single" v-if="values.length &amp;&amp; !isOpen">{{ values.length }} выбрано</span></template>
                <span slot="noResult">Ничего не найдено...</span>
              
                <template slot="option" slot-scope="props">
                  <div class="option">{{ props.option[fieldChoiceText] }}<span v-if="props.option[extraInformationField]" class="text-sm leading-tight text-gray-600"><br>{{ props.option[extraInformationField] }}</span></div>
                </template>
                <template v-slot:noOptions>
                  Загружаем...
              </template>
            </multiselect>
          </div>
    </div>
  </div>
</template>

<script>
  import Multiselect from 'vue-multiselect';
  import CloseCircleOutlineIcon from 'vue-material-design-icons/CloseCircleOutline'
  import { mapGetters } from 'vuex'
  import TransitionLeftRide from '../transitions/leftRide'
  export default {
    props: {
      placeholder: {
        type: String,
      }, 
      fieldChoiceText:{
        type:String
       }, 
      dbValueKey:{
        type: String,
      },
      apiAddress:{
        type: String,
      }, 
      dictKey:{
        type: String,
      }, 
      extraInformationField:{
        type: String,
        default:'',
      },
      trackEveryUpdate:{
        type:Boolean,
        default:false,
      },
      nestedKeys: {
        type: Array,
        default: () => [],
      },
      sendParamName: {
        type: String
      },
      addAction: {
        type: Function
      },
      removeAction:{
        type: Function
      },
      removeKeyAction:{
        type: Function
      },
      initialDbData:{
        type: Object,
        default: () => {},
      }
    },
    data () {
      return {
        value: [],
        options: [],
        hasChange: false,
        showClearAllButton: false,
        // localStorageValues: [],
        // searchValues: [],
      }
    },
    components: {
      Multiselect,
      CloseCircleOutlineIcon,
      TransitionLeftRide
    },
    mounted() {
      // alert(1)
        const axios = require('axios');
        // console.log("NESTED KEYS:")
        // console.log(this.nestedKeys)
        // axios.get('http://127.0.0.1:8000/api/get-streets/').then(resp => {
        //         console.log('RESPONSE DATA: ')
        //         console.log(resp)
        // });
        axios.get(this.apiAddress).then(resp => {

            if(this.nestedKeys.length == 0){
              // this.setActiveValues()
              this.options = resp.data[this.dictKey];
              // this.setActiveValues()
              // console.log('OPTIONS: ')
              // console.log(this.options)
              console.log('RESPONSE DATA: ')
              console.log(resp.data)
            }
            else{
              this.options = []
              this.nestedKeys.forEach((element) => {
              this.options.push(resp.data[this.dictKey][element])
            })
            }
            if(this.sendParamName in this.activeFindParams){
              this.setIntitialActiveValues()
              if(this.value.length > 0){
                this.showClearAllButton = true
              }
            }
        });
    },
    methods: {
      setIntitialActiveValues(){
        console.log('Param name while mounted(' + this.sendParamName+') :',this.activeFindParams[this.sendParamName])
          this.activeFindParams[this.sendParamName].forEach(activeParam => {
            this.options.forEach(element => {
              if(activeParam == element[this.dbValueKey]){
                this.value.push(element)
              }
            })
          })
          
      },
      clearAll () {
        this.value = []
        this.removeKeyAction(this.sendParamName)
        this.hasChange = true
        if(this.trackEveryUpdate){
          this.$emit('removeAll')
        }
        this.SelectCloseAction()
      },
      SelectValueAction(selectedValue){
        this.addAction({'key':this.sendParamName, 'value':selectedValue[this.dbValueKey]})
        this.hasChange = true
        if(this.trackEveryUpdate){
          this.$emit('select', selectedValue[this.dbValueKey])
        }
      },
      removeValueAction(removedValue){
        this.hasChange = true
        this.removeAction({'key':this.sendParamName , 'value':removedValue[this.dbValueKey]})
        if(this.trackEveryUpdate){
          this.$emit('remove', removedValue[this.dbValueKey])
        }
      },
      SelectCloseAction() {
        if(this.hasChange){
          this.hasChange = false
          this.$emit('selectClose', this.dictKey , this.searchValues)
          if(this.value.length > 0){
            this.showClearAllButton = true
          }
          else{
            this.showClearAllButton = false
          }
        }
      },
    },
    computed: {
      ...mapGetters([
        'activeFindParams'
      ]),
    },
  }
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style> 

<style scoped>

/* .multiselect--active { 
  z-index: 20
}
.multiselect__content-wrapper { z-index: 20 } */

</style>

