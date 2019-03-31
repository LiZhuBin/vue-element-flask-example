<template>
  <el-carousel :interval="4000" type="card" height="300px">
    <el-carousel-item v-for="item in bookItems" :key="item">

      <img v-bind:src=item.img height="100%">
        <div style="float:right " >
          <h1>{{ item.title }}</h1>
          <span></span>
          <h1>{{item.sub1}}</h1>

            <h3>{{item.catalog}}</h3>
            <h3>{{item.tag}}</h3>
            <h3>{{item.reading}}</h3>
            <h3>{{item.bytime}}</h3>
        </div>


    </el-carousel-item>
  </el-carousel>
</template>

<script>
    export default {
        name: "BooksHome",
      created:function(){
          this.$http.get(this.GLOBAL.URL_BOOKS+'getBooksContent/'+this.$route.query.id)
        .then(response=>{
          console.log(response.data);
          this.bookItems = response.data.result.data;
        })
      },
      data() {
        return {
          bookItems:[]
        }
      },
      methods:{

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
