<template>
  <div>
    {{ value }}
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
    @remove="removeTagAction"
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
        regularExpr: /\d+[а-я]?/g,
        }
    },
    methods: {
        addTag (newTag) {
        const matches = newTag.match(this.regularExpr)
        // console.log(matches)
        matches.forEach((tagVal) => {
            console.log(this.value.some((elem) => elem[this.searchKey] == tagVal))
            if(!(this.value.some((elem) => elem[this.searchKey] == tagVal))){
                const tag = {}
                tag[this.searchKey] = tagVal
                this.value.push(tag)
            }
            })

        // for(tag in matches){
        //     const tag = {}
        //     tag[this.searchKey] = newTag
        //     this.value.push(tag)
        // }
        // const tag = {}
        // tag[this.searchKey] = newTag
        // this.value.push(tag)
        this.addTagAction()
        },

        addTagAction() {
            this.searchValues = []
            this.value.forEach(element => this.searchValues.push(element[this.searchKey]));
            this.$emit('addTag', this.searchKey , this.searchValues)
       },
        removeTagAction(){
            this.searchValues = []
            this.value.forEach(element => this.searchValues.push(element[this.searchKey]));
            // alert(this.searchValues[tag])
            this.$emit('removeTag', this.searchKey , this.searchValues)
        }
    //   removeTag(tag)
    }
}
</script>