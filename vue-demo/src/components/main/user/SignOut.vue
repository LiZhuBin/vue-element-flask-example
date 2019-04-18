<template>
<div>
  <div>fdffffff</div>
  <el-dialog title="注册" :visible.sync="dialogFormVisible">

    <el-form :model="form">
      <el-form-item label="姓名">
        <el-input v-model="form.name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="姓别">
        <el-switch v-model="form.delivery"></el-switch>
      </el-form-item>
      <el-form-item label="密码">
        <el-radio v-model="sex" label="1">男</el-radio>
        <el-radio v-model="sex" label="2">女</el-radio>
      </el-form-item>
      <el-form-item label="再次输入密码">
        <el-input v-model="form.password" show-password></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">

      <el-button @click="dialogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="singIn">确 定</el-button>
      <el-button type="primary" @click="singOut">注册</el-button>
    </div>


  </el-dialog>
</div>
</template>

<script>
  export default {
    name: "SignOut",
    data() {
      return {
        dialogFormVisible: true,
        userData: {name: '', password: '', sex: '1'}
      }
    }
  }
</script>

<style scoped>

</style>
