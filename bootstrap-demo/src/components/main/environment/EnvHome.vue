<template>
  <div>

      <el-container>

<Slide></Slide>
        <el-main>
          <router-view :key="$route.fullPath"></router-view>
        </el-main>
      </el-container>
    </div>
</template>

<script>
    import Slide from './EnvSlide'


    export default {
        name: "EnvHome",
      components:{
          Slide,
      },

      data(){
          return{
            isRouterAlive: true
          }
      },
      methods:{
      }
    }

</script>

<style scoped>

</style>
