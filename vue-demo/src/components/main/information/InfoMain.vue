<template>

  <div >
    <!--      news modules    -->
    <div>

    <div>
      <h1>最新新闻
        <span style="float:right">
        <el-button type="primary" icon="el-icon-d-arrow-right" circle @click.native="newsClick()">

        </el-button></span></h1>

    </div>

      <el-carousel  type="card" >
    <el-carousel-item  v-for="(app_new,index) in news" v-if="index<6">
       <el-card :body-style="{ padding: '10px' } " shadow="always"  @click.native="exChange(app_new.url)" >
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
    </el-carousel-item>
  </el-carousel>
</div>
<div>
  <el-badge></el-badge>
<!--  books modules   -->
 <div>
      <h1>书箱推荐
        <span style="float:right">
        <el-button type="primary" icon="el-icon-d-arrow-right" circle @click.native="bookClick()">

        </el-button></span></h1>

    </div>
  <div class="grid-content bg-purple">
  <el-row :gutter="20" :space="10">
    <template v-for="(bookItem, index) in this.bookItems" v-if="index<9">
      <el-col :span="6" >
      <el-card >
        <img v-bind:src=bookItem.img height="100%"  >
      </el-card>
    </el-col>
    </template>

  </el-row></div>

</div>
  </div>
</template>b

<script>
  export default {
    "name": "InfoMain",
    "created": function () {
      this.initData();
    },
    "data"() {
      return {
        "newsUrl": this.GLOBAL.URL_NEWS + 'getnews/' + this.$route.query.types,
        "bookUrl": this.GLOBAL.URL_BOOKS + 'getBooksContent/' + this.$route.query.id,
        "news": [],
        "bookItems": [],
      }
    },
    "methods": {
      "initData": function () {
        this.$http.get(this.newsUrl)
          .then(response => {
            this.news = response.data.result.data;
          });
        this.$http.get(this.bookUrl)
          .then(response => {
            console.log(response.data);
            this.bookItems = response.data.result.data;
          })
      },
      "newsClick": function () {
        this.$router.push({"path": '/info/news/top/', "query": {"types": 'top'}})
      },
      'bookClick':function(){
        this.$router.push({'path':'/info/books/'+'252','query':{'id':252}})
      },
      exChange:function(url){
        console.log("ffffffff");
                window.location.href = url
      }

    }
  }
</script>

<style scoped>
  @import "../../style/AppCarousel.css";
  @import "../../style/BookLayout.css";

</style>
