<template>
  <div>
      {{ activeFindParams }}
      {{ value }}
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
</template>

<script>
import Multiselect from 'vue-multiselect'
import { mapGetters } from 'vuex'

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
        // initialDbData: {
        //     type: Array,
        //     default: () => undefined,
        // }
    },
    components: {
        Multiselect
    },

    data () {
        return {
            value: [],
            options: [],
            regularExpr: /\d+[а-я]?/g,
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
       },

    },
    computed: {
    ...mapGetters([
        'activeFindParams'
        ])
       },
}
</script>