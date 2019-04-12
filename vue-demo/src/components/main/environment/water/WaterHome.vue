<template>
<div>
  <el-container>
  <el-header>
   <div >按监测站点查找</div>
    <el-cascader
      :options="options"

      @change="handleItemChange"
    ></el-cascader>
  </el-header>
    <el-main>

 <div>基础信息</div>
      <el-badge></el-badge>
     <div >{{profile}}</div>
       <div> 祥细信息</div>
    <el-table
      :data="tableData"
      border
      style="width: 100%">

      <el-table-column
        prop="state"
        label="state"
      >
      </el-table-column>
      <el-table-column
        prop="ph"
        label="ph"
      >
      </el-table-column>
      <el-table-column
        prop="phquality"
        label="phquality"
      >
      </el-table-column>
      <el-table-column
        prop="oxygen"
        label="oxygen"
      >
      </el-table-column>
      <el-table-column
        prop="oxygenquality"
        label="oxygenquality"
      >
      </el-table-column>
      <el-table-column
        prop="nitrogen"
        label="nitrogen"
      >
      </el-table-column>
      <el-table-column
        prop="nitrogenquality"
        label="nitrogenquality">
      </el-table-column>
       <el-table-column
        prop="permangan"
        label="permangan">
      </el-table-column>
    </el-table>
    <el-badge></el-badge>
    <el-table
      :data="tableData"
      border
      style="width: 100%">

      <el-table-column
        prop="permanganquality"
        label="permanganquality"
      >
      </el-table-column>
      <el-table-column
        prop="orgacarbon"
        label="orgacarbon"
      >
      </el-table-column>
      <el-table-column
        prop="orgacarbonquality"
        label="orgacarbonquality"
      >
      </el-table-column>
      <el-table-column
        prop="section"
        label="section"
      >
      </el-table-column>
      <el-table-column
        prop="belong"
        label="belong"
      >
      </el-table-column>
      <el-table-column
        prop="date"
        label=date
      >
      </el-table-column>
      <el-table-column
        prop="time"
        label="time">
      </el-table-column>
    </el-table>


    </el-main>
    </el-container>
</div>
</template>

<script>
    export default {
       mounted:function(){
        this.init()
      },
     data() {
      return {
        options: [],
        profile: '',
        tableData: []
      };
    },



        methods:{
          init:function(){
            var self = this;
            self.$http.get(this.GLOBAL.URL_WATER+'getstation')
              .then(response=>{
                 this.options= response.data;
              })
            .catch(error=>{
            console.log(error)
          })
          },
          handleItemChange(val) {
            this.$http.get('water/getstation/usestation',{
              params:{
                state:val[0]
              }

            }).then(response=>{
              console.log(response.data);
              this.tableData = response.data.result;
              this.profile = this.tableData[0].profile;
            })

      }
        }
    }
</script>

<style scoped>

</style>
