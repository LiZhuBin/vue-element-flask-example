<template>
  <div>
  <el-carousel :interval="4000" type="card" height="300px" >
    <el-carousel-item v-for="item in bookItems" :key="item" @change = 'carouselChange(item.sub2)'>

      <img v-bind:src=item.img height="100%">
      <div style="float:right ">
        <h1>{{ item.title }}</h1>
        <span></span>
        <h1>{{item.sub1}}</h1>

        <h1>{{item.catalog}}</h1>
        <h1>{{item.tag}}</h1>
        <h1>{{item.reading}}</h1>
        <h1>{{item.bytime}}</h1>
      </div>


    </el-carousel-item>

  </el-carousel>
      <div>
      {{this.contents}}
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
        contents:''
      }
    },
    methods: {
      carouselChange:function (item) {
        this.contents = item;
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
