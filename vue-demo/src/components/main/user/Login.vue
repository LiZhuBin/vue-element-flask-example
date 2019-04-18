<template>

  <div id="app">
<div>

</div>
    <el-dialog title="Sign In" :visible.sync="dialogFormVisible">

      <el-form :model="form">
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码" :label-width="formLabelWidth">
          <el-input   v-model="form.password" show-password ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">

        <el-button @click="exit">取 消</el-button>
        <el-button type="primary" @click="singIn">确 定</el-button>
        <el-button type="success" @click="singOut">注册</el-button>
      </div>


    </el-dialog>
  </div>
</template>

<script>
  import Date from '../../Date.vue'

  export default {
    name: 'login',
     inject:  ['reload'],
    mounted: function () {
      this.getAjax();
    },
    data() {
      return {
        dialogFormVisible: true,
        form: {
          name: 'abc',
          password: '123',
        },
        formLabelWidth: '120px',
        alive: true
      }

    },
    components: {
      Date
    },

    methods: {
exit:function(){
  this.$message('请登录');
},
      singIn: function () {
        this.dialogFormVisible = false;
        this.$router.push({
          path: '/',

        });
        this.$http({
          method: 'post',
          headers: {},
          usl: this.GLOBAL.URL_ROOT + 'login/',
          data: this.qs.stringify({
            name: this.form.name,
            password: this.form.password,
          })
        });
        //message
      this.$message({
        message:'登录成功',
        type:'success'
      })
      },

 singOut:function(){
          //注册
    this.$message('暂不可用');
   // this.dialogFormVisible = false;
          // this.$router.replace({path:'/user/signout', name:'SignOut'})
      }

    }
  }
</script>

<style>
</style>
