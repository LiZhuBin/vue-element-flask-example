import Main from './components/main.vue'
import Login from './App'
import Bycity from './components/fragment/environment/weather/WeatherHome'
import ByStation from './components/fragment/environment/water/WaterHome'
import EnvHome from './components/fragment/environment/EnvHome'
import InfoHome from './components/fragment/infomation/InfoHome'
import NewsHome from './components/fragment/infomation/news/NewsHome'
import BooksHome from './components/fragment/infomation/books/BooksHome'
import WeChatHome from './components/fragment/infomation/wechatnews/WeChatNewsHome'
import SportHome from './components/fragment/sport/SportHome'
import BasketBallHome from './components/fragment/sport/basketball/BasketBallHome'
import TeamView from './components/fragment/sport/basketball/TeamView'

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
      name: 'newsHome',
      path: 'news/:type',
      component: NewsHome
    },
      {
        name: 'bookHome',
        path: 'books/:id',
        component: BooksHome
      },
      {
        name: 'weChatHome',
        path: 'weChat',
        component: WeChatHome
      }
    ]

  },
  {
    path: '/sport/',
    component: SportHome,
    children: [{
      name: 'BasketBallHome',
      path: 'basketBallHome/',
      component: BasketBallHome,
      children: []

    },
      {
        name: 'TeamView',
        path: 'BasketBall/TeamView',
        component: TeamView,
      }
    ]

  },
  {
    path: '/login',
    component: Login
  },


];
export default routers
