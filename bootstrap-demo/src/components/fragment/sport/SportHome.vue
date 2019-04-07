<template>
<el-container>
  <SportSlide></SportSlide>
   <el-main>
          <router-view v-if="isRouterAlive"></router-view>
        </el-main>
</el-container>
</template>

<script>
  import SportSlide from './SportSlide'
    export default {
        name: "SportHome",
         provide() { // 注册一个方法
    return {
      reload: this.reload
    }},
      data(){
          return{
               isRouterAlive: true
        }
      },
      components:{
          SportSlide,
      },
      methods:{
             reload :function(){
      this.isRouterAlive = false;
      this.$nextTick(function() {
        this.isRouterAlive = true;
        console.log('reload')
      })
    }

      }
    }


</script>

<style scoped>

</style>
