<template>
  <div>
    
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
        options: []
        }
    },
    methods: {
        addTag (newTag) {
        const tag = {}
        tag[this.searchKey] = newTag
            // label: newTag
            // name: newTag,
            // code: newTag.substring(0, 2) + Math.floor((Math.random() * 10000000))
        // }
        // this.options.push(tag)
        this.value.push(tag)
        this.updateBuildingsAction()
        },
        updateBuildingsAction() {
            this.searchValues = []
            this.value.forEach(element => this.searchValues.push(element[this.searchKey]));
            // console.log(this.searchValues)
            // alert(this.searchValues)
            this.$emit('update', this.searchKey , this.searchValues)
      }
    }
}
</script>