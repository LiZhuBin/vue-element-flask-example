import Main from './components/main.vue'
import Login from './App'
import Bycity from './components/fragment/environment/weather/WeatherHome'
import ByStation from './components/fragment/environment/water/WaterHome'

const routers = [
  {
    path:'/',
  },
  {
    path: '/login',
    component:Login
  },
  {
    path:'/weather/bycity',
    component: Bycity
  },
  {
    path:'/water/bystation',
    component: ByStation
  }
];
export default routers
