<template>  
    <div>
        <!-- <vHeaderMain v-if=""/>
        <vHeaderLittle v-else/> -->
        <section class="pb-20 -mt-32">
            <div class="container mx-auto px-8">
                <BuildingsSearchKit/>
                <BuildingsList/>
            </div>
        </section>
    </div>
</template>

<script>

// import vHeaderMain from '../components/v-header-main'
// import vHeaderLittle from '../components/v-header-little'
import BuildingsList from '../components/v-buildings-list'
import BuildingsSearchKit from '../components/v-buildings-search-kit'
import { mapActions, mapGetters ,mapMutations } from 'vuex'

export default {

    // data(){
    //     return {
    //         isMainPage: true
    //     }
    // },
    // watch:{
    //   $route: (path) =>{
    //       if(path !== "/"){
    //           this.isMainPage = true
    //       }
    //       else{
    //           this.isMainPage = false
    //       }
    //   }
    // },
    components: {
        BuildingsList,
        BuildingsSearchKit,
        // vHeaderMain,
        // vHeaderLittle
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
        ]),
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
        ]),
        // isMainPage(){
        //     console.log(this.$router.currentRoute)
        //     if(this.$router.currentRoute.path == "/"){
        //         return true
        //     }
        //     else{
        //         return false
        //     }
        // }
    },
}
</script>