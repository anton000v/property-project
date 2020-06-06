<template>  
    <div>
        <Header/>
        <section class="pb-20 bg-gray-300 -mt-32">
            <div class="container mx-auto px-8">
                <BuildingsSearchKit/>
                <BuildingsList/>
            </div>
        </section>
    </div>
</template>

<script>

import Header from '../components/v-header'
import BuildingsList from '../components/v-buildings-list'
import BuildingsSearchKit from '../components/v-buildings-search-kit'
import { mapActions, mapGetters ,mapMutations } from 'vuex'

export default {
    // props:{
    //     findParams: {
    //         type: Object,
    //         default: function () { return {} }
    //     }
    // },
    components: {
        BuildingsList,
        BuildingsSearchKit,
        Header
    },
    methods: {
        // parseFindParams(){
        //     const params = {}
        //     var vars = this.findParams.split('&');
        //     for (var i = 0; i < vars.length; i++) {
        //     var pair = vars[i].split('=');
        //     if(decodeURIComponent(pair[0]) in params){
        //         params[pair[0]].push(decodeURIComponent(pair[1]))
        //     }
        //     else{
        //         params[pair[0]] = [decodeURIComponent(pair[1])]
        //     }
        //     console.log("\tGETTER FIND PARAMS:")
        //     console.log(params)
        //     // params[]decodeURIComponent()
        //     // if (decodeURIComponent(pair[0]) == variable) {
        //     //     return decodeURIComponent(pair[1]);
        //     // }
        //     }
        // },
        ...mapActions([
            'searchBuildings', 
            'actionUpdateFindParams'
        ]),
        ...mapMutations([
            'updateFindParams',
        ])
    },
    // mounted() {
        // alert('Mounted')
        // this.findParams
    //   alert(this.findParams)
        // if(Object.keys(this.findParams).length > 0){
            
        // }
        // else{

        // }
        // console.log('FIND PARAMS:')
        // console.log(this.findParams)
        // if(Object.keys(this.activeFindParams).length === 0){
        //     // alert('empty')
        //     console.log('FIND PARAMS:')
        //     // this.updateFindParams(this.findParams)
        //     console.log(this.$route.query)

            // const copy = Object.assign({}, this.findParams)
            // console.log('COPIED:')
            // console.log(copy)
            // this.updateFindParams(this.$route.query)
            // this.actionUpdateFindParams(this.$route.query)
            // console.log()
        // this.parseFindParams()
            // this.searchBuildings(this.$route.query)

        // }
    
        // console.log('NEW FIND PARAMS AFTER SEARCH:')
        // console.log(this.activeFindParams)        
    // },
    // computed: {
    // //   ...mapGetters([
    // //     'updateFindParams', 
    // //     ])
    // },
    computed: {
      ...mapGetters([
        'activeFindParams', 
        ])
    },
}
</script>