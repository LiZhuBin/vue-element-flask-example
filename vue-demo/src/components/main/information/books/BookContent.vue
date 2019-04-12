<template>
    <el-card>
      <div style="float:right "  >
        <h1>{{ this.item.title }}</h1>
        <span></span>
        <div>{{this.item.sub1}}</div>
        <el-badge></el-badge>
        <div>{{this.item.catalog}}</div>
        <div>{{this.item.tag}}</div>
        <div style="float:bottom">
          {{this.item.reading}}
        {{this.item.bytime}}
          </div>
      </div>
      <div>{{this.item}}</div>
    </el-card>
</template>

<script>
    export default {
        name: "BookContent",
      data(){
          return{
            item :[],
          }
      }
    }
</script>

<style scoped>

</style>
