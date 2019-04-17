<template>
    <div>

      <el-container>
           <InfoSlide></InfoSlide>
        <el-main>
          <router-view v-if="isRouterAlive">
          </router-view>
        </el-main>
      </el-container>
    </div>
</template>

<script>
  import NewsHome from './news/NewsHome'
  import InfoSlide from './InfoSlide'
    export default {
        name: "InfoHome",
       provide() { // 注册一个方法
    return {
      reload: this.reload
    }
  },
       components:{
         InfoSlide,
      NewsHome,
    },
    data(){
          return{
            isRouterAlive: true
          }
    },
    methods: {
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
