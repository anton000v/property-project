<template>
    <div class="text-center text-lg text-myMint-300 hover:text-myMint-100 font-bold transition duration-500">
        <div class="text-gray-500">Найдено:</div> 
        <div ref="buildingsCounter" class="text-4xl">{{ animatedNumber }}</div>
    </div>
</template>

<script>
import {mapGetters} from 'vuex'
import {TweenLite} from 'gsap'
export default {
    props:{
        countByBuildingsArr: {
            type:Boolean,
            default:false
        }
    },

    data(){
        return {
            numberOfBuildings: 0
        }
    },
    computed: {
        ...mapGetters(['allBuildings' ,'buildingsCount']),
        animatedNumber: function() {
            return this.numberOfBuildings.toFixed(0);
        },
        count(){
            if(this.countByBuildingsArr){
                return this.allBuildings.length
            }
            return this.buildingsCount
        }
    },
    methods:{
        animateCounter(val){
            TweenLite.to(this.$data, { 
                duration: 0.5,
                numberOfBuildings: val,
                });
        }
    },
    watch: {
        count: function(val) {
            this.animateCounter(val)
        }
    },
    mounted(){
        if(this.count > 0){
            this.animateCounter(this.count)
        }
    },
}
</script>