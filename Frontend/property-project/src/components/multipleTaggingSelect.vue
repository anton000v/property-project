<template>
  <div>
    <!-- <p>{{ value }}</p>
    <p>{{ searchValues }}</p> -->
    <!-- <label class="typo__label">{{ searchKey }}</label> -->
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
        начните ввод
    </template>
    </multiselect>
    <!-- <pre class="language-json"><code>{{ value  }}</code></pre> -->

  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'

// export default {
//   components: {
//     Multiselect
//   },
//   data () {
//     return {
//       value: [
//         { name: 'Javascript', code: 'js' }
//       ],
//       options: [
//         { name: 'Vue.js', code: 'vu' },
//         { name: 'Javascript', code: 'js' },
//         { name: 'Open Source', code: 'os' }
//       ]
//     }
//   },
//   methods: {
//     addTag (newTag) {
//       const tag = {
//         name: newTag,
//         code: newTag.substring(0, 2) + Math.floor((Math.random() * 10000000))
//       }
//       this.options.push(tag)
//       this.value.push(tag)
//     }
//   }
// }
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
        // searchKey: {
        //   type: String,
        // }
    },
    components: {
        Multiselect
    },

    data () {
        return {
            value: [],
            options: [],
            searchValues: [],
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
                    vm.searchValues.push(tagVal);
                }
                })
            vm.changeTagAction()
        // this.value.forEach(element => this.searchValues.push(element[this.searchKey]));
        // for(tag in matches){
        //     const tag = {}
        //     tag[this.searchKey] = newTag
        //     this.value.push(tag)
        // }
        // const tag = {}
        // tag[this.searchKey] = newTag
        // this.value.push(tag)
        // this.changeTagAction()
        },

        deleteTagAction(deletedTag){
            let index = this.searchValues.indexOf(deletedTag[this.searchKey]);
            // console.log(deletedTag)
            // console.log(this.searchValues)
            // alert(index)
            if (index > -1) {
                this.searchValues.splice(index, 1);
            }
        // this.value.forEach(element => this.searchValues.push(element[this.searchKey]));
            this.changeTagAction()
        },

        changeTagAction() {
            // this.value.forEach(element => this.searchValues.push(element[this.searchKey]));
            this.$emit('tagsChange', this.searchKey , this.searchValues)
       },
        // removeTagAction(){
        //     this.searchValues = []
        //     this.value.forEach(element => this.searchValues.push(element[this.searchKey]));
        //     // alert(this.searchValues[tag])
        //     this.$emit('removeTag', this.searchKey , this.searchValues)
        // }
    //   removeTag(tag)
    }
}
</script>