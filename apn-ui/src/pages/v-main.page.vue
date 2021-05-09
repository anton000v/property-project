<template>
  <div>
    <div>
      <vShortManual></vShortManual>
    </div>
    <div class="mt-20">
      <vSearchPage/>
    </div>
  </div>
</template>

<script>
import vSearchPage from '../pages/v-search-buildings-page'
import vShortManual from '../components/v-short-manual'

export default {
  components: {
    vSearchPage,
    vShortManual
  }
}
</script>