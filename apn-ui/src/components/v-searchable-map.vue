<template>
  <div>
      <v-map 
        :zoom=10.5
        :center="initialLocation"
        :style="'height:50vh; z-index: 0;'"
  
        >
        <v-icondefault></v-icondefault>
        <v-tilelayer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></v-tilelayer>
        <v-marker-cluster :options="clusterOptions" @clusterclick="click()" @ready="ready">
          <!-- <v-marker v-for="l in locations" :key="l.id" :lat-lng="l.latlng" :icon="icon">
            <v-popup :content="l.text"></v-popup>
          </v-marker> -->
          <v-marker v-for="building in buildings" :key="building.slug" :lat-lng="getLatLng(building.lat, building.lng)"  :icon="icon">
            <v-popup>
              <div class="w-auto md:w-64">
                <div class="w-full grid grid-col-1 py-2 m-1">
                  <div v-if="building.administrative_district != null" class="inline-flex items-center">
                    <HomeCityIcon class="text-myHeaderColor" :size="17"  />
                    <div class="flex-1 sm:px-1 px-2 text-base">
                      Район: {{ building.administrative_district }}
                    </div>
                  </div>
                  <div v-if="building.district != null" class="inline-flex items-center">
                    <HomeGroupIcon class="text-myHeaderColor" :size="17" />
                    <div class="flex-1 sm:px-1 px-2 text-base">
                        {{ building.district }}
                    </div>
                  </div>
                  <div v-if="building.micro_district !== 'Не делится на микрорайоны'" class="inline-flex items-center">
                    <DomainIcon class="text-myHeaderColor" :size="17" />
                    <div class="flex-1 sm:px-1 px-2 text-base">
                        {{ building.micro_district }}
                    </div>
                  </div>
                  <div v-if="building.developer != null" class="inline-flex items-center">
                    <HouseEditIcon class="text-myHeaderColor" :size="17" />
                    <div class="flex-1 sm:px-1 px-2 text-base">
                        {{ building.developer }}
                    </div>
                  </div>
                  <div class="grid grid-cols-1 md:grid-cols-2 text-center gap-2">
                    <router-link :to="{name:'building-page', params:{slug:building.slug}}">
                      <p class="border cursor-pointer rounded-lg  text-black shadow text-sm md:transition md:duration-500 md:transform md:hover:translate-y-1 md:ease-in-out text-center block  md:hover:shadow-lg py-2">
                        Открыть
                      </p>
                    </router-link>
                      <p @click="show(building.slug)" class="hidden md:block border cursor-pointer rounded-lg  text-black shadow text-sm md:transition md:duration-500 md:transform md:hover:translate-y-1 md:ease-in-out text-center block  md:hover:shadow-lg py-2">
                        Предпросмотр
                      </p>
                  </div>
                  <!-- <div class="grid grid-cols-2 gap-2">
                    <div class="text-center bg-myHeaderColor">
                      <p class="text-white text-sm">
                        Открыть
                      </p>
                    </div>
                    <div class="text-center bg-myHeaderColor">
                      <p class="text-white text-sm">
                        Предпросмотр
                      </p>
                    </div>
                  </div> -->
              </div>
            </div>
            </v-popup>
          </v-marker>
        </v-marker-cluster>
      </v-map>
      <vBuildingPreview v-for="building in buildings" :key="building.slug" :slug="building.slug" :building="building"/>
  </div>
</template>

<script>
  import * as Vue2Leaflet from 'vue2-leaflet'
  // import L from 'leaflet';
  // delete L.Icon.Default.prototype._getIconUrl;
  import { latLng, Icon, icon } from 'leaflet'
  import Vue2LeafletMarkercluster from 'vue2-leaflet-markercluster'
  import iconUrl from 'leaflet/dist/images/marker-icon.png'
  import shadowUrl from 'leaflet/dist/images/marker-shadow.png'
  import {mapGetters} from 'vuex'
  import HouseEditIcon from 'vue-material-design-icons/HomeEdit';
  import HomeCityIcon from 'vue-material-design-icons/HomeCity';
  import HomeGroupIcon from 'vue-material-design-icons/HomeGroup';
  import DomainIcon from 'vue-material-design-icons/Domain';
  import vBuildingPreview from '../components/v-building-preview'

  export default {
    props:{
      'buildings': Array
    },
    components: {
      'v-map': Vue2Leaflet.LMap,
      'v-tilelayer': Vue2Leaflet.LTileLayer,
      'v-icondefault': Vue2Leaflet.LIconDefault,
      'v-marker': Vue2Leaflet.LMarker,
      'v-popup': Vue2Leaflet.LPopup,
      'v-marker-cluster': Vue2LeafletMarkercluster,
      HouseEditIcon,
      HomeCityIcon,
      HomeGroupIcon,
      DomainIcon,
      vBuildingPreview
    },
    methods: {
      click: (e) => console.log("clusterclick", e),
      ready: (e) => console.log('ready', e),
      getLatLng(lat, lng){
        // console.log(lat+' '+lng)
        if(lat && lng){
          return latLng(lat, lng)
        }
        console.log('null')
        return null
      },
      show (slug) {
        this.$modal.show('building-preview:'+slug);
      },
      hide (slug) {
          this.$modal.hide('building-preview:'+slug);
      },
    },
    data () {
      // let locations = []
      // for (let i = 0; i < 100; i++) {
      //   locations.push({
      //     id: i,
      //     latlng: latLng(rand(-34.9205), rand(-57.953646)),
      //     text: 'Hola ' + i
      //   })
      // }
      let customicon = icon(Object.assign({},
        Icon.Default.prototype.options,
        {iconUrl, shadowUrl}
      ))
      return {
        // locations,
        icon: customicon,
        clusterOptions: {},
        initialLocation: latLng(49.988358, 36.232845),
        latLng: latLng
        // L:L
      }
    },
    mounted() {
      setTimeout(() => {

        console.log('done')
        this.$nextTick(() =>{
          this.clusterOptions = { disableClusteringAtZoom: 11 }
        });
      }, 5000);
    },
    computed:{
      ...mapGetters(['allBuildings']),
    }
  }
</script>

<style>
  @import "~leaflet/dist/leaflet.css";
  @import "~leaflet.markercluster/dist/MarkerCluster.css";
  @import "~leaflet.markercluster/dist/MarkerCluster.Default.css";

</style>