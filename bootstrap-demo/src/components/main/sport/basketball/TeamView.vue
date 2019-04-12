<template>
  <div>


    <el-tabs :tab-position="tabPosition" style="height: 200px;">
      <el-tab-pane label="队伍简介信息">
        <el-card>
          <div>
            <img v-bind:src="team.logo_link">
            <h1>{{team.full_name}} /{{team.eng_full_name}} ({{team.name}}/{{team.eng_name}})</h1>
          </div>
           <div>建立时间:{{team.found_year}}</div>
          <div>{{team.intro}}</div>
          <div>队伍链接:
            <a v-bind:href="team.m_team_link">{{team.m_team_link}}</a> </div>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="队伍信息">
        <el-card>
          <div>
            <el-tag >home
            </el-tag>
            {{team.home}}
            <a v-bind:href="team.homepage_link">{{team.homepage_link}}</a>
          </div>

          <div>
            <el-tag>cn_division</el-tag>
            {{team.cn_division}}
          </div>
          <div>
            <el-tag>chief_coach</el-tag>
            {{team.chief_coach}}
          </div>

        </el-card>
      </el-tab-pane>
      <el-tab-pane label="体育錧信息">
        <el-table :data="team.stadiumsInfo">
          <el-table-column
          prop="name"
          label="name">

          </el-table-column>
          <el-table-column
          prop="eng_name"
          label="eng_name">

          </el-table-column>
          <el-table-column
          prop="city"
          label="city">

          </el-table-column>
          <el-table-column
          prop="state"
          label="state">

          </el-table-column>
          <el-table-column
          prop="capacity"
          label="capacity">

          </el-table-column>
        </el-table>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
  export default {
    name: "TeamView",
    created: function () {
      this.initData(this.$route.query.id)
    },
    methods: {
      initData: function (id) {
        this.team.id = id;

        this.$http.get(this.GLOBAL.URL_SPORT + 'basketball/getTeam/' + id)
          .then(response => {
            console.log(response.data);
            this.team = response.data;
          })
      }
    },
    data() {
      return {
        tabPosition: 'top',
        team: {}      }
    }

  }
</script>

<style scoped>

</style>
