<template>
        <!-- <div class="asfdsf"> -->
            <vue-picture-swipe :ref="gallaryRef" :options="{shareEl: false, history:false, captionEl:true, class:'dasds'}" :items="preparedImages"
            >
            </vue-picture-swipe>
        <!-- </div> -->
        <!-- <button @onclick="sh">safdsfdf</button> -->

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
/* img[itemprop="thumbnail"]{ */
    /* padding: 5px; */
    /* width: 500px; */
    /* height:auto; */
    /* display: inline-block; */
/* } */

/* 
.my-gallery{
    display: grid;
    grid-template-columns: repeat(2, minmax(250px, 1fr));
    grid-gap: 2vw;
} */


/* @media (min-width: 768px) {  */
.my-gallery{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));

}
/* } */
/* @media (min-width: 768px) { 
    .my-gallery{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
}
}

@media (min-width: 1024px) { 
    .my-gallery{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
}
}
 @media (min-width: 1280px) { 
    .my-gallery{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
}
}  */

</style>