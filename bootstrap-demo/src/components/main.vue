<template>
  <div>
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-header style="text-align: right; font-size: 12px">

        <Head></Head>

      </el-header>
    <router-view></router-view>


    </el-container>


  </div>
</template>

<script>
  import Head from './Head.vue'

  export default {
    methods: {},
    components: {
      Head,

    },


  }

</script>
export default {

}
<style scoped>

</style>
