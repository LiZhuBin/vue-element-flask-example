<template>
  <div id="app">
    <div>
      <router-view v-if="alive"/>
    </div>

    <el-dialog title="Sign In" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="Name" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Password" :label-width="formLabelWidth">
          <el-input v-model="form.password" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">

        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="singIn">确 定</el-button>
      </div>


    </el-dialog>
    <Date></Date>
    <router-view></router-view>
  </div>
</template>

<script>
  import Date from './components/Date.vue'

  export default {
    name: 'login',
    mounted: function () {
      this.getAjax();
    },
    data() {
      return {
        dialogFormVisible: true,
        form: {
          name: '',
          password: '',
        },
        formLabelWidth: '120px',
        alive: true
      }

    },
    components: {
      Date
    },

    methods: {

      singIn: function () {
        this.dialogFormVisible = false;
        this.$router.push({
          path: '/home',

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

      },
      getAjax: function () {
        this.$http.get('http://127.0.0.1:5000/login/', {

          headers: {},
        })

          .then(function (response) {
            console.log(response.data);

          })
          .catch(function (error) {
            console.log(error);
          });
      },


    }
  }
</script>

<style>
</style>
