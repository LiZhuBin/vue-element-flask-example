<template>
  <div>
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-header style="text-align: right; font-size: 12px">

        <Head></Head>

      </el-header>
      <el-container>

        <Slide></Slide>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>


    </el-container>


  </div>
</template>

<script>
  import Head from './fragment/Head.vue'
  import Slide from './fragment/environment/EnvSlide.vue'

  export default {
    methods: {},
    components: {
      Head,
      Slide,

    },


  }

</script>
export default {

}
<style scoped>

</style>
