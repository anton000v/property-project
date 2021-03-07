<template>
    <transition :name="transitionName">
        <slot></slot>
    </transition >
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    props: { 
        of: {
            type: String,
            default: null
        }
    },
    data() {
        return {  
            transitionName: '',
            isCurrentPageChanged: false,
            isBuildingsCountChanged: false,
            curPage: 0,
        }
    },
    computed: {
      ...mapGetters([
            'currentBuildingPage',
            'flatsCurrentPage',
            'flatsCount',
            'buildingsCount',
            'showFlatsOnly'
        ]),
        // actualTransitionName() {
        //     if(this.isBuildingsCountChanged){
        //         // this.isBuildingsCountChanged = false
        //         return 'newSearch'
        //     }
        //     if(this.isCurrentPageChanged){
        //         // this.isCurrentPageChanged = false
        //         return 'newPage'
        //     }
        //     return ''
        // },
        currentPage(){
            
            if(this.of == 'flats'){
                
                return this.flatsCurrentPage
                
            }
            else if(this.of == 'buildings'){
                return this.currentBuildingPage
            }
            else{
                console.log(`\tERROR! Передано неправильное значение(${this.of}) в ключ of (list transition)`)
                return false
            }
        }
    },
    watch: {
        currentPage: function(val) {
            // alert('New page')
            // this.isCurrentPageChanged = true
            if(this.curPage > val){
                // alert('bigger')
                this.transitionName = 'newPageLeft'
            }
            else if (this.curPage < val){
                // alert('less')
                this.transitionName = 'newPageRight'
            }
            this.curPage = val
            
        },
        buildingsCount: function () {
            this.transitionName = 'newSearch'
            //  alert('buildings count')
            // this.isBuildingsCountChanged = true
        },
        flatsCount: function() {
            // alert('changeFlatsCount')
            this.transitionName = 'newSearch'
        }


    },
}
</script>

<style scoped>

/* .cards-enter-active {
  transition: opacity 0.5s linear, transform 0.4s linear;
}
.cards-enter{
    transform: translateY(100vh);
    opacity: 0;
} */

.newSearch-enter-active {
  transition: opacity 0.5s linear, transform 0.3s linear;
}
.newSearch-enter{
    transform: translateY(20px);
    opacity: 50%;
}
.newSearch-leave-active {
    /* transform: translateY(-15px); */
    /* transition: opacity .2s linear */
    /* transition: opacity 0.05s linear, transform 0.3s linear; */
}
.newSearch-leave-to {
    /* transform: translateY(-5px); */
    /* opacity: 40%; */
    /* transform: translateY(-15px); */
    /* transform: translateY(-30px); */
    /* opacity: 50%; */
}


.newPageRight-enter-active {
  transition: opacity 0.4s linear, transform 0.2s linear;
}
.newPageRight-enter{
    transform: translateX(5vw);
    opacity: 10%;
}


.newPageLeft-enter-active {
  transition: opacity 0.4s linear, transform 0.2s linear;
}
.newPageLeft-enter{
    transform: translateX(-5vw);
    opacity: 10%;
}

</style>