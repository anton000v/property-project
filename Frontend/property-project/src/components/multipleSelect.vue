<template>
  <div> 
      <!-- <label class="typo__label">Simple select / dropdown</label> -->
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
          
          selectLabel="enter чтобы выбрать" 
          deselectLabel="enter чтобы удалить" 
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
          <!-- <template slot="tag" slot-scope="{ option, remove }">
              <span >
                <span>{{ option[extraInformationField] }}
                  </span>
                  <span class="multiselect__remove" @click="remove(option)">❌</span>
              </span>
            </template> -->
          <!-- <template slot="tag" slot-scope="props">
            <div class="tag">{{ props.option[fieldChoiceText] }}</div>
          </template> -->
        </multiselect>
      <!-- <pre class="language-json"><code>{{ value  }}</code></pre> -->
  </div>
</template>

<script>
  // import { ModelSelect } from 'vue-search-select'
  import Multiselect from 'vue-multiselect';
  import { baseApiAddress } from '../variables.js';

  export default {
    // model: {
    //   event: 'change',
    //   // event: 'updateBuildings'
    // },
    props: {
      placeholder: {
        type: String,
      }, 
      fieldChoiceText:{
        type:String
       }, 
      searchKey:{
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
      // receivedOptions:{
      //   type: Array,
      //   default: () => [],
      // },
      nestedKeys: {
        type: Array,
        default: () => [],
      },
    },
    data () {
      return {
        value: [],
        options: [],
        // options: [
        //         { id: -1},
        //       ][0][this.choiceText] = 'Пожалуйста, подождите...',  
          // apiAddress:apiAddress,
        searchValues: [],
      }
    },
    components: {
      Multiselect
    },
    mounted() {
        const axios = require('axios');
        // console.log("Address: " + baseApiAddress + this.apiAddress)
        axios.get(baseApiAddress + this.apiAddress).then(resp => {
          
            if(this.nestedKeys.length == 0){
              this.options = resp.data[this.dictKey];
            }
            else{
              this.options = []
              // console.log(resp.data[this.dictKey]['not_divided'])
              

            //  console.log(resp.data[this.dictKey])
              // console.log(this.nestedKeys)
              // console.log(resp.data[this.dictKey]['not_divided'])
              // this.options searchValues: [],= []
              this.nestedKeys.forEach((element) => {
              this.options.push(resp.data[this.dictKey][element])
              // numCallbackRuns++
            })

              // console.log(this.options)
            }

            // console.log(this.apiAddress + " " +resp.data[this.dictKey]);
        });
    },
    methods: {
      clearAll () {
        this.value = []
      },
      // nameWithExtraInformation(option){
      //   if(this.extraInformationField) {
      //     // console.log(this.extraInformationField)
      //     return `${option[this.fieldChoiceText]} (${option[this.extraInformationField]})`
      //   }
      //   else{
      //     return option[this.fieldChoiceText]
      //   }
      // },

      // updateValueAction () {
      //   this.$emit('change', this.value)
      //   // console.log(this.value[this.searchKey])
      // },
      SelectValueAction(selectedValue){
        this.searchValues.push(selectedValue[this.searchKey]);
        // console.log('Pushed value')

        if(this.trackEveryUpdate){
          // alert(selectedValue)
          this.$emit('select', selectedValue[this.searchKey])
          // const selectedValues = []
          // this.value.forEach(element => selectedValues.push(element[this.searchKey]));
          // this.$emit('input', selectedValues)
        }
      },
      removeValueAction(removedValue){
        let index = this.searchValues.indexOf(removedValue[this.searchKey]);
        // console.log(index)
        if (index > -1) {
            this.searchValues.splice(index, 1);
        }
        if(this.trackEveryUpdate){
          // alert(removedValue)
          this.$emit('remove', removedValue[this.searchKey])
        }
      },
      SelectCloseAction() {
        // this.searchValues = []
        // this.value.forEach(element => this.searchValues.push(element[this.searchKey]));
        this.$emit('selectClose', this.dictKey , this.searchValues)
      }
    },
  }
</script>

<!-- New step!
     Add Multiselect CSS. Can be added as a static asset or inside a component. -->
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>