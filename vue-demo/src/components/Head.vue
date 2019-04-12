<template>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
  <el-menu-item  v-for="(item,index) in this.menus"  @click.native="menuClick(item.menuRouter)">
    {{item.title}}
    </el-menu-item>
</el-menu>
</template>

<script>
  export default {
    name: "Head",

    data() {
      return {
        activeIndex: '1',
        menus: [
          {title: '环境', menuRouter: '/'},
          {title: '信息', menuRouter: '/info'},
          {title: '体育', menuRouter: '/sport'},
        ],

      }

    },
    methods: {
      menuClick: function (menuRouter) {
        this.$router.push(menuRouter)
      }
    }
  }
</script>

<style scoped>
  .router-link-active {
    text-decoration: none;
  }

</style>
