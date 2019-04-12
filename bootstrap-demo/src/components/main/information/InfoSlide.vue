<template>
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-message"></i>时讯</template>
        <el-menu-item-group v-for="item in newsItems">

          <el-menu-item>

            <router-link :to="{path:'/info/news/'+item.itemValue+'/',query:{types:item.itemValue}}"
                          @click.native="viewReload">{{item.itemName}}
            </router-link>
          </el-menu-item>
        </el-menu-item-group>


      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>图书</template>

        <el-menu-item-group>

          <el-menu-item v-for="item in bookItems">
              <router-link :to="{path:'/info/books/'+item.id,query:{id:item.id}}" @click.native="viewReload">
                {{item.catalog}}
              </router-link>
          </el-menu-item>

        </el-menu-item-group>

      </el-submenu>

      <el-submenu index="3">
        <template slot="title"><i class="el-icon-menu"></i>微信精选</template>
        <el-menu-item-group>
          <el-menu-item>
                    <router-link :to="{name:'weChatHome',query:{pno:1,ps:20}}" @click.native="viewReload" >微信精选</router-link>

          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="4">
        <template slot="title"><i class="el-icon-menu"></i>笑话</template>
        <el-menu-item-group>
          <el-menu-item>
                <router-link :to="{name:'jokes' ,query:{id:1,page:1,pagesize:20}} " @click.native="viewReload" >最新笑话</router-link>
          </el-menu-item>
          <el-menu-item>
            <router-link :to="{name:'randomJokes' } " @click.native="viewReload" >随机笑话</router-link>
          </el-menu-item>
        </el-menu-item-group>

      </el-submenu>
    </el-menu>
  </el-aside>
</template>

<script>
  export default {
    name: "InfoSlide",
     inject:  ['reload'],
    mounted: function () {
      this.intiData()
    },
    data() {
      return {
        newsItems: [
          {
            itemValue: 'top',
            itemName: '头条'
          },
          {
            itemValue: 'shehui',
            itemName: '社会'
          },
          {
            itemValue: 'guonei',
            itemName: '国内'
          },
          {
            itemValue: 'guoji',
            itemName: '国际'
          },
          {
            itemValue: 'yule',
            itemName: '娱乐'
          },
          {
            itemValue: 'tiyu',
            itemName: '体育'
          },
          {
            itemValue: 'junshi',
            itemName: '军事'
          },

          {
            itemValue: 'keji',
            itemName: '科技'
          },
          {
            itemValue: 'caijing',
            itemName: '财经'
          },
          {
            itemValue: 'shishang',
            itemName: '时尚'
          }
        ],
        bookItems: []
      }
    },
    methods: {
      intiData: function () {
        this.$http.get(this.GLOBAL.URL_BOOKS + 'getBooksType')
          .then(response => {
            this.bookItems = response.data;
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
