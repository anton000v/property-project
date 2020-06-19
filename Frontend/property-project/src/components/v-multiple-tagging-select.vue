<template>
  <div>
      <div class="flex items-center">
        <TransitionLeftRide>
          <div class='flex-1 px-1 cursor-pointer text-sm transition duration-500 ease-in-out  hover:opacity-40 transform hover:-translate-y-1 hover:-rotate-90 text-myMint-400 hover:text-myMint-100' v-show="showClearAllButton" @click="clearAll">
              <CloseCircleOutlineIcon :size="20"  title="Очистить все"/>
          </div>
        </TransitionLeftRide>
        <multiselect 
        v-model="value" 
        :tag-placeholder="tagPlaceHolder" 
        :placeholder="placeholder" 
        :label="searchKey" 
        :track-by="searchKey" 
        :options="options" 
        :multiple="true" 
        :taggable="true"
        @tag="addTag"
        @remove="deleteTagAction"
        >
        <template v-slot:noOptions>
            просто вводите
        </template>
        </multiselect>
    </div>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'
import { mapGetters } from 'vuex'
import TransitionLeftRide from '../transitions/leftRide'
import CloseCircleOutlineIcon from 'vue-material-design-icons/CloseCircleOutline'
export default {
    props: {
        placeholder: {
            type: String,
        }, 
        tagPlaceHolder: {
            type: String,
        },
        searchKey: {
            type: String,
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
        // initialDbData: {
        //     type: Array,
        //     default: () => undefined,
        // }
    },
    components: {
        Multiselect,
        CloseCircleOutlineIcon,
        TransitionLeftRide
    },

    data () {
        return {
            value: [],
            options: [],
            regularExpr: /\d+[а-я]?/g,
            showClearAllButton: false,
        }
    },
    mounted(){
        // alert(1)
        if(this.sendParamName in this.activeFindParams){
            // alert()
            // console.log(this.activeFindParams[this.sendParamName])
            // this.setIntitialActiveValues()
            this.value = this.activeFindParams[this.sendParamName]
        }
    },
    methods: {
        // setIntitialActiveValues(){
        //     console.log('AAA')
        //     console.log(this.activeFindParams[this.sendParamName])
        //     this.activeFindParams[this.sendParamName].forEach(activeParam => {
        //         this.value.push(activeParam)

        //         // this.options.forEach(element => {
        //         // if(activeParam === element[this.dbValueKey]){
        //         //     this.value.push(element)
        //         // }
        //         // })
        //     })
        // },
        addTag (newTag) {
            let vm = this;
            const matches = newTag.match(vm.regularExpr)
            let isUnique = false 
            matches.forEach((tagVal) => {
                // console.log(tagVal in  vm.value)
                // console.log(vm.value)
                // if(!(tagVal in vm.value)){
                tagVal = parseInt(tagVal)
                if(vm.value.indexOf(tagVal) == -1){
                    // const tag = {}
                    // tag[vm.sendParamName] = tagVal
                    if(!isUnique){
                        isUnique = true
                    }
                    vm.value.push(tagVal)
                    vm.addAction({'key': vm.sendParamName, 'value':tagVal})
                }
                })
            if(isUnique){
                this.changeTagAction()
            }
            
        },

        deleteTagAction(deletedTag){
            this.removeAction({'key':this.sendParamName, 'value':deletedTag})
            
            this.changeTagAction()
        },

        changeTagAction() {
            this.$emit('tagsChange')
            if(this.sendParamName in this.activeFindParams){
                if(this.activeFindParams[this.sendParamName].length > 0){
                    this.showClearAllButton = true
                    return
                }
            }
            this.showClearAllButton = false
       },
        clearAll () {
            this.value = []
            this.removeKeyAction(this.sendParamName)
            this.changeTagAction()
      },

    },
    computed: {
    ...mapGetters([
        'activeFindParams'
        ])
       },
}
</script>