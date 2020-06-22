<template>
    <modal 
    ref='googleMapModal'
    name="google-map-modal"
    width="1920"
    height="auto"
    :adaptive="true"
    :scrollable="true"
    @opened="googleMapOpened"
    >
       <div ref="modalBody" v-dynamic="messageAsHtml">
            {{ text }}
       </div>
    </modal>
</template>

<script>
export default {
    props: {
        url: String,
    },
    data() {
        return{
            text: 'hi #linky'
        }
    },
    // mounted() {
    //     this.$nextTick(() => {
    //         //     alert(this.$refs["anchors-default-position"].offsetTop )
    //         // var url = "/abc.html?myselection="+id; //or anyother html page
    //         // console.log('REFS:')
    //         // console.log(this.$refs)
    //         this.$refs.googleMapModal['modalBody'].$el = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" src="'+this.url+'"></iframe>';
    //     })
    // },
    // created() {
    //     console.log('AFTER CREATED')
    //     console.log(this.$refs)
    // },
    methods:{
        googleMapOpened(){
            

            // this.$refs.modalBody.$el = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" src="'+this.url+'"></iframe>';
            // console.log(this.$refs.modalBody)
            // this.$refs.modalBody.innerText = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" src="'+this.url+'"></iframe>';
            // this.$compile(this.$refs.modalBody);
            // console.log(this.$refs.modalBody)
        }
    },
    directives:{
        dynamic(newValue) {
            this.el.innerHTML = newValue;
            this.vm.$compile(this.el);
        }
    },
    messageAsHtml: function() {
      return this.text.replace(/#(\S*)/g, '<a v-on:click="someAction()">#$1</a>');
    }

}
</script>

<style scoped>
    /* .vm--overlay {
    background: red;
    } */
</style>

