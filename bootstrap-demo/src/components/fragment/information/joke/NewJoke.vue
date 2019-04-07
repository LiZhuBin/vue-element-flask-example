<template>
  <div>
    <el-steps direction="vertical" :active=this.pageSize>
      <div v-for="item in content">
        <el-step :title="item.content" :description=item.source></el-step>
      </div>
    </el-steps>
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="page"
      :page-size="pageSize"
      :page-sizes="[20, 30, 40,50]"
      layout="total, sizes, prev, pager, next, jumper"
    >
    </el-pagination>
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
        pageSize: 20
      }
    },
    methods: {
      initData: function (id, page, pagesize) {

        this.page = parseInt(page);
        this.pageSize = parseInt(pagesize);
        this.id = parseInt(id);
        console.log(this.pageSize);
        this.$http.get('info/jokes/getNewJoke/',
          {
            params: {
              id: this.id, page: this.page, pagesize: this.pagesize
            }
          })
          .then(response => {
            console.log(response.data);
            this.content = response.data.result.data;

          })
      },
      handleSizeChange(val) {
        this.pageSize = parseInt(val);
        this.initData(self.id,self.page,self.pagesize);
        this.$router.push({path: '/info/jokes/getNewJoke/', params: {id: this.id, page: this.page, pagesize: this.pagesize}});
        this.reload();
      },
      handleCurrentChange(val) {
        this.page = parseInt(val);
        console.log(`当前页: ${val}`);
        this.$router.push({path: '/info/jokes/getNewJoke/', params: {id: this.id, page: this.page, pagesize: this.pagesize}});
        this.reload()
      }
    }


  }
</script>

<style scoped>

</style>
