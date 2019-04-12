<template>
  <el-card>
<!--    头   -->
    <div style="text-align:center" slot="header">
    <el-button type="primary" round @click="changeContents" >换一批</el-button>

      </div>
<!--    内容    -->
    <el-steps direction="vertical" :active=50>
      <div v-for="item in contents">
        <el-step :title="item.content"></el-step>
        <el-badge></el-badge>
      </div>
    </el-steps>

  </el-card>
</template>

<script>

  export default {

    name: "RandomJoke",
     inject: ['reload'],
    mounted: function () {
      this.init();
    },
    data() {
      return {
        getContentUrl: '/info/jokes/getRandomJoke/',
        contents: []
      }
    },
    methods: {
      init: function () {
        this.$http.get(this.getContentUrl)
          .then(response => {
            this.contents = response.data.result;
          })
      },
      changeContents:function(){

        this.reload()
      }
    },



  }
</script>

<style scoped>

</style>
