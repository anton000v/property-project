<template>
    <div>
        <vue-picture-swipe :options="{shareEl: false, history:false, captionEl:true}" :items="preparedImages"
        >
        </vue-picture-swipe>
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
        }
    },
    components:{
        VuePictureSwipe
    },
    data(){
        return{
             
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
            return imgs
        },

       
    },
}
</script>

<style>
img[itemprop="thumbnail"]{
    padding: 5px;
    width: 500px;
}
</style>