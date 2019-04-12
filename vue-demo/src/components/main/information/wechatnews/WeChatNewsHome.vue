<template >
  <div>
  <el-steps direction="vertical" :active= this.pageSize >
    <div v-for="item in content">
    <el-step :title="item.title" :description=item.source ></el-step>
      </div>
  </el-steps>
  <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-size="pageSize"
      :page-sizes="[20, 30, 40,50]"
      layout="total, sizes, prev, pager, next, jumper"
      >
    </el-pagination>
    </div>
</template>

<script>
    export default {
        name: "WeChatNewsHome",
           inject:  ['reload'],
      created:function(){

          this.initData(this.$route.query.ps,this.$route.query.pno)
      },
      data(){
          return{
            currentPage:1,
            content:[],
            pageSize:20
          }
      },
      methods:{
        initData:function (size,pno) {
              this.currentPage = pno;
              this.pageSize = size;
                this.$http.get(this.GLOBAL.URL_WECHATNEWS+'getBooksContent/'+size+'/'+pno)
        .then(response=>{
          this.content = response.data.result.list;
        })
    },
       handleSizeChange(val) {
        this.pageSize = val;
        this.$router.push({path:'/info/weChat/',query:{pno:val,ps:this.pageSize}});
       this.reload();
      },
      handleCurrentChange(val) {
        this.currentPage = val;
        console.log(`当前页: ${val}`);
        this.$router.push({path:'/info/weChat/',query:{pno:val,ps:this.pageSize}});
         this.reload()
      }
        }

    }

</script>

<style scoped>

</style>
