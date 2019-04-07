<template>
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu v-for="items in menus">
      <el-submenu>
        <template slot="title">{{items.name}}</template>
        <el-menu-item v-for="item in items.data">
          <router-link :to="{name :'TeamView' ,query:{'id':item.id}}" @click.native="viewReload">{{item.name}}
          </router-link>
        </el-menu-item>
      </el-submenu>
    </el-menu>
  </el-aside>
</template>

<script>
  export default {
    name: "SportSlide",
 inject:  ['reload'],
    created: function () {
      this.init();
    },
    data() {
      return {
        menus:
          [
            {
              'name': "NBA球队详细信息",
              'data': [{'id': '', 'name': ''}]
            }
          ]

      }
    },
    methods: {
      init: function () {
        this.$http.get(this.GLOBAL.URL_SPORT + 'basketball/getTeamName')
          .then(response => {
            console.log(response.data);
            this.menus[0]['data'] = response.data;

          })
      },
     viewReload: function () {
      this.reload()
      }
    }
  }
</script>

<style scoped>

</style>
