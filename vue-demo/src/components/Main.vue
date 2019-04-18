<template>

  <div>
    <SignIn></SignIn>
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
  import SignIn from './main/user/Login'

  export default {
        provide() {
      return {
        reload: this.reload
      }
    },
     reload() {
        this.alive = false;
        this.$nextTick(() => {
          this.alive = true
        })
      },
    methods: {},
    components: {
      Head,
      SignIn,

    },


  }

</script>
export default {

}
<style scoped>

</style>
