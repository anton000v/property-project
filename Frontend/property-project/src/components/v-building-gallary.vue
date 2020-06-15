<template>
    <div>
        <vue-picture-swipe :ref="gallaryRef" :options="{shareEl: false, history:false, captionEl:true}" :items="preparedImages"
        >
        </vue-picture-swipe>
        <!-- <button @onclick="sh">safdsfdf</button> -->
    </div>
</template>

<script>
import VuePictureSwipe from 'vue-picture-swipe';

export default {
    props:{
        images_src:{
            type: Array,
        },
        caption: {
            type: String
        },
        gallaryRef:{
            type:String,
            default: ''
        }
    },
    components:{
        VuePictureSwipe
    },
    data(){
        return{
        //     pswp: Object 
        }
    },
    computed: {
        preparedImages(){
            let imgs = []
            this.images_src.forEach(element => {
                imgs.push({
                    src:element,
                    thumbnail:element,
                    w: 1600,
                    h: 900,
                    title: this.caption
                })
            });
            console.log(imgs)
            return imgs
        },

       
    },
    // methods: {
    //     al(){
    //         // alert()
    //         //  console.log(this.pswp)
    //     }
    // },
}
</script>

<style>
img[itemprop="thumbnail"]{
    padding: 5px;
    width: 500px;
    height:auto;
    display: inline-block;
}

/* a[itemprop="contentUrl"]{
    padding: 5px;
    width: 500px;
} */
</style>