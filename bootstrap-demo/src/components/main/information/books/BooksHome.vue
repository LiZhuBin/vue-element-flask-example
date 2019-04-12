<template>
  <div>
  <el-carousel :interval="4000" type="card" height="300px" @change = 'carouselChange'>
    <el-carousel-item v-for="item in bookItems" :key="item" >
<el-container>
      <img v-bind:src=item.img height="100%">
  <el-main>
      <div style="float:right "  >
        <h1>{{ item.title }}</h1>
        <span></span>
        <div>{{item.sub1}}</div>
        <el-badge></el-badge>
        <div>{{item.catalog}}</div>
        <div>{{item.tag}}</div>
        <div style="float:bottom">
          {{item.reading}}
        {{item.bytime}}
          </div>
      </div>
    </el-main>
</el-container>

    </el-carousel-item>

  </el-carousel>
<div>

  <el-card >
    <div slot="header">
      <h1>图书简介</h1>
    </div>
   <div> {{this.currentItem.sub2}}</div>
  </el-card>
</div>
    </div>
</template>

<script>
  export default {
    name: "BooksHome",
inject: ['reload'],

    created: function () {

      this.$http.get(this.GLOBAL.URL_BOOKS + 'getBooksContent/' + this.$route.query.id)
        .then(response => {
          console.log(response.data);
          this.bookItems = response.data.result.data;
        })
    },
    data() {
      return {
        bookItems: [],
        currentItem : '',
        contents:''
      }
    },
    methods: {
      carouselChange:function (item,item2) {
        this.currentItem = this.bookItems[item];
        this.contents = this.currentItem.sub2
      }
    }
  }
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
