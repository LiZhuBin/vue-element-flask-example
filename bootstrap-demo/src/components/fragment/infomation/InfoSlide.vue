<template>
<el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu >
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-message"></i>时讯</template>
        <el-menu-item-group v-for="item in newsItems">

         <el-menu-item >

			<router-link  :to="{path:'/info/news/'+item.itemValue,query:{types:item.itemValue}}" @click.native="clickRouterLink()">{{item.itemName}}</router-link>
         </el-menu-item>
        </el-menu-item-group>


      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>图书</template>

        <el-menu-item-group>

          <el-menu-item v-for="item in bookItems">

			<li><router-link  :to="{path:'/info/books/'+item.id,query:{id:item.id}}" @click.native="clickRouterLink()">{{item.catalog}}</router-link></li>
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
        name: "InfoSlide",
      mounted:function(){
         this.intiData()
      },
       data(){
          return {
            newsItems :[
              {
                itemValue:'top',
                itemName:'头条'
              },
              {
                itemValue:'shehui',
                itemName:'社会'
              },
              {
                itemValue:'guonei',
                itemName:'国内'
              },
              {
                itemValue:'guoji',
                itemName:'国际'
              },
              {
                itemValue:'yule',
                itemName:'娱乐'
              },
              {
                itemValue:'tiyu',
                itemName:'体育'
              },
              {
                itemValue:'junshi',
                itemName:'军事'
              },

              {
                itemValue:'keji',
                itemName:'科技'
              },
              {
                itemValue:'caijing',
                itemName:'财经'
              },
              {
                itemValue:'shishang',
                itemName:'时尚'
              }
            ],
            bookItems:[]
          }
       },
       methods:{
          clickRouterLink () {
      if (typeof (Storage) !== 'undefined') {
        if (localStorage.selected) {
          // 存储
          localStorage.selected = this.selected
        } else {
          // 创建Web Storage
          localStorage.selected = 1
        }
      } else {
        console.log('抱歉！您的浏览器不支持 Web Storage ...')
      }
      // 页面刷新
      location.reload()
    },
          intiData:function () {
            this.$http.get(this.GLOBAL.URL_BOOKS+'getBooksType')
              .then(response=>{
                this.bookItems  = response.data;
              })
          }
       }
    }
</script>

<style scoped>

</style>
