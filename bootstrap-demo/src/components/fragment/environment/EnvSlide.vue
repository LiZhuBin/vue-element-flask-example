<template>
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['1', '3']" >
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-message"></i>天气</template>
        <el-menu-item-group>
<template slot="title">天气质量查看</template>
         <el-menu-item >

			<router-link  to="/weather/bycity" >按城市查找</router-link>
         </el-menu-item>
        </el-menu-item-group>


      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>水质量</template>

        <el-menu-item-group>
          <template slot="title">水质量查看</template>
          <el-menu-item >

			<li><router-link  to="/water/bystation" >按站点查看</router-link></li>
         </el-menu-item>

        </el-menu-item-group>

        </el-submenu>

      <el-submenu index="3">
      </el-submenu>
    </el-menu>
  </el-aside>
</template>

<script>

    export default {
      created() {
        this.$store.state.adminleftnavnum = "2-2"; //设置左侧导航2-2 active
      },
      name: "Slide",


    }

</script>

<style scoped>

</style>
