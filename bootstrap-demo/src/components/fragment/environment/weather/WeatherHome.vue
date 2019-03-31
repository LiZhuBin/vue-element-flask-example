<template>

  <div>
    <el-container>
<el-header>
     <div >select city</div>
     <el-cascader
      :options="options"

      @change="handleItemChange"
    ></el-cascader>
</el-header>
      <el-main>
 <div>now weather</div>
    <el-table
      :data="tableData"
      border
      style="width: 100%">

      <el-table-column
        prop="temperature"
        label="temperature"
      >
      </el-table-column>
      <el-table-column
        prop="humidity"
        label="humidity"
      >
      </el-table-column>
      <el-table-column
        prop="info"
        label="info"
      >
      </el-table-column>
      <el-table-column
        prop="wid"
        label="wid"
      >
      </el-table-column>
      <el-table-column
        prop="direct"
        label="direct"
      >
      </el-table-column>
      <el-table-column
        prop="power"
        label="power"
      >
      </el-table-column>
      <el-table-column
        prop="aqi"
        label="aqi">
      </el-table-column>
    </el-table>
    <el-badge></el-badge>
     <div>future weather</div>
    <el-table
      :data="futureWeather"
      border
      style="width: 100%">


      <el-table-column
        prop="date"
        label="date"
      >
      </el-table-column>
      <el-table-column
        prop="direct"
        label="direct"
      >
      </el-table-column>
      <el-table-column
        prop="temperature"
        label="temperature"
      >
      </el-table-column>
      <el-table-column
        prop="weather"
        label="weather"
      >
      </el-table-column>

    </el-table>
        </el-main>
      </el-container>
  </div>
</template>

<script>

  export default {
    mounted: function () {
      this.citySet()
    },

    data() {
      return {
        options: [],
        select_city: '',
        tableData: [],
        futureWeather:[]
      };
    },

    methods: {

      citySet: function () {
        var self = this;
        self.$http.get(this.GLOBAL.URL_WEATHER + 'getcity')
          .then((response) => {
            this.options = response.data;

          })
          .catch(function (error) {
            console.log(error)
          })
      },
      getWeatherByCity: function (val) {

        console.log(val[1]);
        this.$http.get('weather/getweather/usecity', {
            params: {
              city:val[1]
            }
          }
        ).then((response) => {
          console.log(response.data.realtime);
          this.tableData = [response.data.realtime];
          this.futureWeather = response.data.future
        }).catch((error) => {
          console.log(error)
        });

      },
      handleItemChange(val) {
        this.select_city = val[1];
        this.getWeatherByCity(val);

      }
    }
  };
</script>
<style scoped>

</style>
