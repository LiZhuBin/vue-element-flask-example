<template>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
  <el-menu-item index="1">
    <router-link to="/">环境</router-link>
    </el-menu-item>
  <el-menu-item index="2">
    	<li><router-link  to="/info" >信息</router-link></li>
    </el-menu-item>

  <el-menu-item index="3" >体育</el-menu-item>
  <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
</el-menu>
</template>

<script>
    export default {
      data(){
        return{
          activeIndex: '1',
        }

      },
        name: "Head",
      methods:{
            handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
      }
    }
</script>

<style scoped>

</style>
