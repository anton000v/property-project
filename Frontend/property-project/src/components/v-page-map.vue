<template>
<div >
    <div>
      <!-- <p>First marker is placed at {{ lat }}, {{ lng }}</p> -->
      <!-- <p>Center is at {{ currentCenter }} and the zoom is: {{ currentZoom }}</p> -->
      <!-- <button @click="showLongText">
        Toggle long popup
      </button> -->
      <!-- <button @click="showMap = !showMap">
        Toggle map
      </button> -->
    </div>
    <l-map
      v-if="showMap"
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      :style="'height:'+mapSize+'px;'"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker :lat-lng="coords">
        <l-popup>
          <div @click="innerClick">
            I am a popup
            <p v-show="showParagraph">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
              sed pretium nisl, ut sagittis sapien. Sed vel sollicitudin nisi.
              Donec finibus semper metus id malesuada.
            </p>
          </div>
        </l-popup>
      </l-marker>
      <!-- <l-marker :lat-lng="withTooltip">
        <l-tooltip :options="{ permanent: true, interactive: true }">
          <div @click="innerClick">
            I am a tooltip
            <p v-show="showParagraph">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
              sed pretium nisl, ut sagittis sapien. Sed vel sollicitudin nisi.
              Donec finibus semper metus id malesuada.
            </p>
          </div>
        </l-tooltip>
      </l-marker> -->
    </l-map>
  </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";

// ---- For fix bugs
import "leaflet/dist/leaflet.css";
import L from 'leaflet';
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});
//

export default {
  name: "Example",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    // LTooltip
  },
  props: {
      lat: Number,
      lng: Number,
      zoom: Number,
      mapSize: Number,
  },
  data() {
    return {
    //   zoom: 15,
      center: this.coords,
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    //   withPopup: latLng(47.41322, -1.219482),
    //   withTooltip: latLng(47.41422, -1.250482),
      currentZoom: 15,
      currentCenter: false,
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5
      },
      showMap: true
    };
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    // showLongText() {
    //   this.showParagraph = !this.showParagraph;
    // },
    innerClick() {
      alert("Click!");
    },
    
  },
  computed:{
      coords(){
          return latLng(this.lat, this.lng)
      }
  },
  created() {
    this.currentCenter = this.coords;
    this.center = this.coords;
  },
};
</script>