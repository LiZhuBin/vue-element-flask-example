<template>
  <div class="block">
    <span class="demonstration">默认</span>
    <el-date-picker
      v-model="value1"
      type="date"
      placeholder="选择日期">
    </el-date-picker>
  </div>
</template>

<script>
  export default {
    name: "Date",
    data(){
      return{
        value1:"333"
      }
    }
  }
</script>

<style scoped>

</style>
