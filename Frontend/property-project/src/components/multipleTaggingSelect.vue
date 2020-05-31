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
                // console.log(vm.value.some((elem) => elem[vm.searchKey] == tagVal))
                if(!(vm.value.some((elem) => elem[vm.searchKey] == tagVal))){
                    const tag = {}
                    tag[vm.searchKey] = tagVal
                    // alert(tag)
                    vm.value.push(tag)
                    // vm.searchValues.push(tagVal);
                    vm.addAction({'key': vm.searchKey, 'value':tagVal})
                }
                })
            vm.changeTagAction()
        },

        deleteTagAction(deletedTag){
            this.removeAction({'key':this.searchkey, 'value':deletedTag[this.searchKey]})
            this.changeTagAction()
        },

        changeTagAction() {
            this.$emit('tagsChange')
       },
    }
}
</script>