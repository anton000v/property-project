<template>
  <div>
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
    methods: {
        addTag (newTag) {
            let vm = this;
            const matches = newTag.match(vm.regularExpr) 
            matches.forEach((tagVal) => {
                // console.log(tagVal in  vm.value)
                // console.log(vm.value)
                // if(!(tagVal in vm.value)){
                if(vm.value.indexOf(tagVal) == -1){
                    // const tag = {}
                    // tag[vm.sendParamName] = tagVal
                    vm.value.push(tagVal)
                    vm.addAction({'key': vm.sendParamName, 'value':tagVal})
                }
                })
            vm.changeTagAction()
        },

        deleteTagAction(deletedTag){
            this.removeAction({'key':this.sendParamName, 'value':deletedTag})
            this.changeTagAction()
        },

        changeTagAction() {
            this.$emit('tagsChange')
       },
    }
}
</script>