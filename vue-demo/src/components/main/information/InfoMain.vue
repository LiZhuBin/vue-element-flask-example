<template>
  <el-carousel :interval="4000" type="card" >
    <el-carousel-item v-for="item in news"  >
          <img v-bind:src=item.thumbnail_pic_s class="img-responsive" >
    </el-carousel-item>
  </el-carousel>
</template>

<script>
  export default {
    name: "InfoMain",
    created:function(){
      this.initData();
    },
    data() {
      return {

        newsUrl: this.GLOBAL.URL_NEWS + 'getnews/top',
        news: []
    }
    },
    methods: {
      initData: function () {
        this.$http.get(this.newsUrl)
          .then(response => {
            this.news = response.data.result.data;
          })
      }
    }
  }

</script>

<style scoped>
  @import "../../style/AppCarousel.css"

</style>
