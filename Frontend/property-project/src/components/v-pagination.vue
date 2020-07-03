<template>
    <div class='w-full flex pt-16' v-if="pagesNumber > 1">
        <!-- {{ buildingsTotalPages }}
        {{ currentBuildingPage  }}
        {{ nextPageLink }} 
        {{ previousPageLink }} -->
        <!-- {{pagesNumber}} -->
        <paginate
            v-model="page"
            :page-count="pagesNumber"
            :page-range="pageRange"
            :margin-pages="2"
            :click-handler="clickCallback"
            :prev-text="'Назад'"
            :next-text="'Вперед'"
            :hide-prev-next="true"
            container-class="flex list-reset rounded w-auto m-auto font-sans"
            page-class="block border-r border-grey-light px-3 py-2 md:transition md:duration-500 md:ease-in-out hover:opacity-40 md:transform md:hover:-translate-y-1"
            active-class="block text-white bg-myMint-400 border-r px-3 py-2"
            prev-class="pr-8 block border-r border-grey-light px-3 py-2 md:transition md:duration-500 md:ease-in-out md:hover:opacity-40 md:transform md:hover:-translate-y-1"
            next-class="pl-8 block border-r border-grey-light px-3 py-2 md:transition md:duration-500 md:ease-in-out md:hover:opacity-40 md:transform md:hover:-translate-y-1"
            break-view-text="..."
            break-view-class="transition-none transform-none cursor-not-allowed"
            >

        </paginate>
    </div>
</template>
 
<script>
import Paginate from 'vuejs-paginate'
import { mapGetters, mapMutations, mapActions } from 'vuex'
import { addHashToLocation } from '../utils.js'
import { stringToInt } from '../utils'

export default {
    props:{
        of: {
            type: String,
            default: null,
        }
    },
    components:{
        Paginate
    },
    data() {
        return {
            page:  (stringToInt(this.$route.query.page) != -1) ? stringToInt(this.$route.query.page) : 1
        }
    },
    methods: {
        ...mapMutations([
            // 'removeStreet',
            // 'addStreet'
            'addFindParam',
            'removeFindParam',
            'updateFindParams',
            'removeFindParamKey',
        ]),
        ...mapActions([
            'searchBuildings',
            'searchFlats'
        ]),
        clickCallback: async function(pageNum) {
            // var VueScrollTo = require('vue-scrollto');
            // var options = {
            //     // container: 'body',
            //     easing: 'ease-in',
            //     // offset: -60,
            //     force: true,
            //     cancelable: true,
            //     // onStart: function(element) {
            //     // // scrolling started
            //     // },
            //     // onDone: function(element) {
            //     // // scrolling is done
            //     // },
            //     // onCancel: function() {
            //     // // scrolling has been interrupted
            //     // },
            //     x: false,
            //     y: true
            // }
            
            if(this.of == "flats"){
                this.removeFindParamKey('page')
                this.addFindParam({key:'page','value':pageNum})
                this.searchFlats(this.activeFindParams)
                this.scrollUp('flats')
            }
            else if(this.of == 'buildings'){
                this.removeFindParamKey('page')
                this.addFindParam({key:'page','value':pageNum})
                this.searchBuildings(this.activeFindParams)
                this.scrollUp('buildings')
            }
            else{
                console.log(`\tERROR! Передано неправильное значение(${this.of}) в ключ of (v-pagination)`)
                return false
            }
            addHashToLocation(this.activeFindParams, this.$route.path)
            console.log(pageNum)
            // VueScrollTo.scrollTo('#buildings-list-begin', 500, options)
            // var that = this;
            // setTimeout(function (){
            //         that.removeFindParamKey('page')
            //         that.addFindParam({key:'page','value':pageNum})
            //         that.searchBuildings(that.activeFindParams)
            //         // this.callAddHashToLocation()
            //         addHashToLocation(that.activeFindParams, that.$route.path)
            //         console.log(pageNum)
            //         },
            //         500
            //         )

                // (function() {
                
                //     this.removeFindParamKey('page')
                //     this.addFindParam({key:'page','value':pageNum})
                //     this.searchBuildings(this.activeFindParams)
                //     // this.callAddHashToLocation()
                //     addHashToLocation(this.activeFindParams, this.$route.path)
                //     console.log(pageNum)
                //     })
            

           
        },
        callAddHashToLocation() {
          addHashToLocation(this.activeFindParams, this.$route.path)
        },
         scrollUp(type){
            var VueScrollTo = require('vue-scrollto');
            var options = {
                // container: 'body',
                easing: 'ease-in',
                // offset: -60,
                force: true,
                cancelable: true,
                // onStart: function(element) {
                // // scrolling started
                // },
                // onDone: function(element) {
                // // scrolling is done
                // },
                // onCancel: function() {
                // // scrolling has been interrupted
                // },
                x: false,
                y: true
            }
            
            
            // this.removeFindParamKey('page')
            // this.addFindParam({key:'page','value':pageNum})
            // this.searchBuildings(this.activeFindParams)
            // addHashToLocation(this.activeFindParams, this.$route.path)
            VueScrollTo.scrollTo(`#${type}-list-begin`, 500, options)
        }
    },
    computed:{
        ...mapGetters([
            'buildingsCount',
            'buildingsTotalPages',
            'currentBuildingPage',
            'nextPageLink',
            'previousPageLink',
            'activeFindParams',
            'showFlatsOnly',
            // 'elementsPerPage',

            // 'allFlats',
            'flatsCount',
            'flatsTotalPages',
            'flatsCurrentPage',
            'flatsNextPageLink',
            'flatsPreviousPageLink',
            ]),
        pageRange(){
            if(this.of == "flats"){
                if(this.flatsTotalPages < 10){
                    return 7
                }
            }
            else if(this.of == 'buildings'){
                if(this.buildingsTotalPages < 10){
                    return 7
                }
            }
            return 100

            
        },
        pagesNumber(){
            if(this.of == "flats"){
                return this.flatsTotalPages
            }
            else if(this.of == 'buildings'){
                return this.buildingsTotalPages
            }
            else{
                console.log(`\tERROR! Передано неправильное значение(${this.of}) в ключ of (v-pagination)`)
                return false
            }
            
        },
        
    },
    mounted() {
        // alert(this.currentBuildingPage)
    }
}
</script> 