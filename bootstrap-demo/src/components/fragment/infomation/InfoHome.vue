<template>
    <div>

      <el-container>
           <InfoSlide></InfoSlide>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </div>
</template>

<script>
  import NewsHome from './news/NewsHome'
  import InfoSlide from './InfoSlide'
    export default {
        name: "InfoHome",
       components:{
         InfoSlide,
      NewsHome,
    }
    }

</script>

<style scoped>

</style>
