<template>
    <div class="max-w-sm transition duration-500 ease-in-out hover:opacity-40 transform hover:-translate-y-1 hover:scale-110 hover:shadow-2xl rounded-circle overflow-hidden shadow-lg">
      <img v-if="building.building_images[0]" :src="getSrc(building.building_images[0].building_image)" alt="">
      <p v-else>Нету изображения :р</p>
      <div class="flex items-center px-6 py-3 bg-gray-900">
          <!-- <svg class="h-6 w-6 text-white fill-current" viewBox="0 0 512 512">
              <path d="M256 48C150 48 64 136.2 64 245.1v153.3c0 36.3 28.6 65.7 64 65.7h64V288h-85.3v-42.9c0-84.7 66.8-153.3 149.3-153.3s149.3 68.5 149.3 153.3V288H320v176h64c35.4 0 64-29.3 64-65.7V245.1C448 136.2 362 48 256 48z"/>
          </svg> -->
          <h1 class="mx-3 text-white font-semibold text-lg">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</h1>
      </div>
      <div class="px-6 py-4">
        <!-- <div class="font-bold text-xl mb-2">{{ building.street }} {{ building.house_number }}{{ building.house_letter }}</div> -->
          <div class="mt-6 grid m-auto sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 justify-center text-center">
              <div class>
                <p class="text-gray-700 font-bold">{{ building.administrative_district }}
                </p>
                <p class="text-md mt-2 text-gray-600 font-hairline">Административный район
                </p>
              </div>
              <div>
                <p class="text-gray-700 font-bold">{{ building.district }}
                </p>
                <p class="text-md mt-2 text-gray-600 font-hairline">Район
                </p>
              </div>
              <div>
                <p class="text-gray-700 font-bold">{{ building.developer }}
                </p>
                <p class="text-xs mt-2 text-gray-700 font-hairline">Застройщик
                </p>
              </div>
          </div>
      </div>
    </div>
  <!-- <div class=" transition duration-500 ease-in-out bg-white shadow p-4 rounded lg:w-64 hover:opacity-50 hover:bg-red-500 transform hover:-translate-y-1 hover:scale-110">
    <div class="text-center mt-4">
      <p class="text-gray-600 font-bold">Name
      </p>
      <p class="text-sm font-hairline text-gray-600 mt-1">Subtitle
      </p>
    </div>
    <div class="flex justify-center mt-4">
      <img class="shadow sm:w-12 sm:h-12 w-10 h-10 rounded-full" src="" alt="Avatar" />
    </div>
    <div class="mt-6 flex justify-between text-center">
      <div>
        <p class="text-gray-700 font-bold">20
        </p>
        <p class="text-xs mt-2 text-gray-600 font-hairline">Posts
        </p>
      </div>
      <div>
        <p class="text-gray-700 font-bold">99k
        </p>
        <p class="text-xs mt-2 text-gray-600 font-hairline">Likes
        </p>
      </div>
      <div>
        <p class="text-gray-700 font-bold">530
        </p>
        <p class="text-xs mt-2 text-gray-700 font-hairline">Shares
        </p>
      </div>
    </div>
    <div class="mt-6">
      <button class="rounded shadow-md w-full items-center shadow bg-blue-500 px-4 py-2 text-white hover:bg-blue-400">
        Follow
      </button>
    </div>
  </div>
               -->


</template>

<script>
import { baseBackendAddress } from '../variables.js';
console.log(baseBackendAddress);
export default {
  props: ['building'],
  data(){
    return {
      // djangoImagesPathInComponentsFolder:djangoImagesPathInComponentsFolder,
      // testPath:"../../../../Backend/PropertyProject_engine/PropertyProject_api/media/126403.jpg",
      baseBackendAddress,
    }
  },
  methods: {
    getSrc(imgPath) {
        // var images = require.context('../../assets/plants/', false, /\.jpg$/);
        return this.baseBackendAddress + imgPath
    }
  }
}
</script>
