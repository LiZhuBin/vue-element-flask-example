<template>
<el-container>
  <SportSlide></SportSlide>
   <el-main>
     <div>
      <div >按队伍名查找</div>
       <el-input placeholder="请输入内容" v-model="input3" class="input-with-select">
       <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
         </el-input>
     </div>
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
      reload: this.reload,
      options:[]
    }},
      data(){
          return{
               isRouterAlive: true,
            input3:''
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
    },
        search:function () {
          this.$message({
            message:'没有查到',
            type: 'error'
          })
        }

      }
    }


</script>

<style scoped>

</style>
