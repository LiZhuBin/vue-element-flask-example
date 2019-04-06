<template>
  <div>
    <el-row aria-rowspan="3" :gutter="40" :space="2">
      <template v-for="app_new in news">
        <el-col :span="10"  @click.native="newsClick(app_new.url)">
          <el-card :body-style="{ padding: '10px' } " shadow="always"  >
            <div slot="header" class="clearfix">
              {{ app_new.title }}
            </div>
            <div>
              <img v-bind:src=app_new.thumbnail_pic_s class="image">
            </div>
            <div style="float: right">
              <span>来自{{app_new.category}}</span>
              <time class="time">{{ app_new.date }}</time>
            </div>


          </el-card>
        </el-col>
      </template>
    </el-row>

  </div>
</template>

<script>
  export default {
inject: ['reload'],
    created:function(){
   console.log(this.getStatus(this.$route.path));
      this.$http.get(this.GLOBAL.URL_NEWS+'getnews/'+this.$route.query.types)
        .then(response=>{
          this.news = response.data.result.data;
        })
    },
    name: "NewsHome",
    data() {
      return {
        news: []

      }
    },
  methods:{
      newsClick:function (url) {
        console.log(url);
        window.location.href = url

      },
    getStatus (urlStr) {
    var urlStrArr = urlStr.split('/')
    return urlStrArr[urlStrArr.length - 1]
  }
  },
  watch: {
  '$route' (to, from) {
  //刷新参数放到这里里面去触发就可以刷新相同界面了
    this.getStatus(this.$route.path)
  }
}

  }
</script>

<style scoped>

</style>
