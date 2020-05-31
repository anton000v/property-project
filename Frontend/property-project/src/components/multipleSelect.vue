<template>
  <div> 
    <!-- {{ fieldChoiceText }} {{ searchKey }} {{ apiAddress }} {{ dictKey }} -->
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
        </multiselect>
  </div>
</template>

<script>
  import Multiselect from 'vue-multiselect';

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
      addAction: {
        type: Function
      },
      removeAction:{
        type: Function
      },
      // selectedArr:{
      //   type: Array
      // }
    },
    data () {
      return {
        value: [],
        options: [],
        // searchValues: [],
      }
    },
    components: {
      Multiselect
    },
    mounted() {
        const axios = require('axios');
        // console.log("NESTED KEYS:")
        // console.log(this.nestedKeys)
        // axios.get('http://127.0.0.1:8000/api/get-streets/').then(resp => {
        //         console.log('RESPONSE DATA: ')
        //         console.log(resp)
        // });
        axios.get(this.apiAddress).then(resp => {
          
            if(this.nestedKeys.length == 0){
              this.options = resp.data[this.dictKey];
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
        });
    },
    methods: {
      clearAll () {
        this.value = []
      },
      SelectValueAction(selectedValue){
        // this.searchValues.push(selectedValue[this.dbValueKey]);
        this.addAction({'key':this.dictKey, 'value':selectedValue[this.dbValueKey]})
        // alert()
        if(this.trackEveryUpdate){
          this.$emit('select', selectedValue[this.dbValueKey])
        }
      },
      removeValueAction(removedValue){
        this.removeAction({'key':this.dictKey , 'value':removedValue[this.dbValueKey]})
        // let index = this.selectedArr.indexOf(removedValue[this.searchKey]);
        // if (index > -1) {
        //     this.searchValues.splice(index, 1);
        // }
        if(this.trackEveryUpdate){
          this.$emit('remove', removedValue[this.dbValueKey])
        }
      },
      SelectCloseAction() {
        this.$emit('selectClose', this.dictKey , this.searchValues)
      }
    },
  }
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>