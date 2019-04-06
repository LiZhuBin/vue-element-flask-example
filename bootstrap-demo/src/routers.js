import Main from './components/main.vue'
import Login from './App'
import Bycity from './components/fragment/environment/weather/WeatherHome'
import ByStation from './components/fragment/environment/water/WaterHome'
import EnvHome from './components/fragment/environment/EnvHome'
import InfoHome from './components/fragment/infomation/InfoHome'
import NewsHome from './components/fragment/infomation/news/NewsHome'
import BooksHome from './components/fragment/infomation/books/BooksHome'
import WeChatHome from './components/fragment/infomation/wechatnews/WeChatNewsHome'

const routers = [
  {
    path: '/',
    component: EnvHome,
    children: [{
      path: 'weather/bycity',
      component: Bycity,
    },
      {
        path: 'water/bystation',
        component: ByStation
      },

    ]
  },
  {
    path: '/info/',
    component: InfoHome,
    children: [{
      name:'newsHome',
      path: 'news/:type',
      component: NewsHome
    },
      {
        name:'bookHome',
        path:'books/:id',
        component:BooksHome
      },
      {
        name:'weChatHome',
        path:'weChat/:pno',
        component:WeChatHome
      }
    ]

  },
  {
    path: '/login',
    component: Login
  },


];
export default routers
