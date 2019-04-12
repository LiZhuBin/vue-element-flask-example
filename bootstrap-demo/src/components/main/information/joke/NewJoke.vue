<template>

  <div>
<!--    单选    -->

      <el-card>
        <div slot="header">
            <el-radio v-model="radio" label="1" >顺序查看</el-radio>
        </div>

   <div >
    <el-steps direction="vertical" :active=50>
      <div v-for="item in content">
        <el-step :title="item.content" :description=item.source></el-step>
        <el-badge></el-badge>
      </div>
    </el-steps>
     </div>
<!--    分页  -->
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="page"
      :page-size="pageSize"
      :page-sizes="[20, 30, 40,50]"
      layout="total, sizes, prev, pager, next, jumper"
    >
    </el-pagination>
         </el-card>
  </div>
</template>





<script>

  export default {
    name: "NewJoke",
    inject: ['reload'],
    created: function () {

      this.initData(this.$route.query.id, this.$route.query.page, this.$route.query.pagesize)
    },
    data() {
      return {
        id: 1,
        page: 1,
        content: [],
        pageSize: 20,
        radio: '1',
        url : 'info/jokes/getNewJoke/'
      }
    },
    methods: {
      //初始化数据 id 标志位:(1)为得到最新的数据；page:第几页数；pagesize:每页显示的数制数
      initData: function (id, page, pagesize) {

        this.page = parseInt(page);
        this.pageSize = parseInt(pagesize);
        this.id = parseInt(id);
        console.log(this.pageSize);
        this.$http.get(this.url,
          {
            params: {
              id: this.id, page: this.page, pagesize: this.pagesize
            }
          })
          .then(response => {
            this.content = response.data.result.data;

          })
      },
      handleSizeChange(val) {
        //更新数据,局部刷新,pagesize改变时启动
        this.pageSize = parseInt(val);
        this.$router.push({path: '/info/jokes', query: {id: this.id, page: this.page, pagesize: val}});
        this.reload();
      },
      handleCurrentChange(val) {
        //更新数据,局部刷新,page改变时启动
        this.page = parseInt(val);
        this.$router.push({path: '/info/jokes', query: {id: this.id, page: val, pagesize: this.pagesize}});
        this.reload()
      }
    },
 components: {

    },

  }
</script>

<style scoped>

</style>
