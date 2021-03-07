<template>
    <div>
        <!-- {{ value }} -->
        <input v-model="value" class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none "  :class="{'border-myMint-300' : typing}"
            id="username" 
            type="number" 
            pattern='[0-9]*' 
        > 
    </div>
</template>

<script>
import _ from 'lodash';
import { mapGetters } from 'vuex'
export default {
    props:{
        sendParamName: String,
        addAction : Function,
        // removeAction : Function,
        removeKeyAction : Function,
        isForExtendedSearch:{
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            value: null,
            typing: false
        }
    },
    // mounted(){
    //     console.log(_.random(20))
    // },
    created: function () {
    // _.debounce — это функция lodash, позволяющая ограничить то,
    // насколько часто может выполняться определённая операция.
    // В данном случае мы ограничиваем частоту обращений к yesno.wtf/api,
    // дожидаясь завершения печати вопроса перед отправкой ajax-запроса.
    // Узнать больше о функции _.debounce (и её родственнице _.throttle),
    // можно в документации: https://lodash.com/docs#debounce

        this.debouncedGetAnswer = _.debounce(this.getAnswer, 500)
    },
    watch: {
    // эта функция запускается при любом изменении вопроса
        value: function () {
            this.typing = true
            this.debouncedGetAnswer()
            
        }
    },
    methods: {
        getAnswer: function () {
            this.typing = false
            if(this.value > 0){
                this.removeKeyAction(this.sendParamName)
                this.addAction({'key':this.sendParamName, 'value':this.value})
                this.$emit('valueChanged')
            }
            else{
                this.value = null
                this.removeKeyAction(this.sendParamName)
                this.$emit('valueChanged')
            }
        }
    },
    computed: { 
        ...mapGetters([
        'activeFindParams'
      ]),
    },
    mounted() {
        if(this.sendParamName in this.activeFindParams){
            if(this.activeFindParams[this.sendParamName].length == 1){
                this.value = this.activeFindParams[this.sendParamName][0]
                if(this.isForExtendedSearch == true){
                  // alert(1)
                  this.$emit('activateExtendedSearch')
                }
            }
            // else if(this.activeFindParams[this.sendParamName].length != 0){
            //     this.removeKeyAction()
            // }
        }
    }
}
</script>