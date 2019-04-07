import Main from './components/main.vue'
import Login from './App'
import Bycity from './components/fragment/environment/weather/WeatherHome'
import ByStation from './components/fragment/environment/water/WaterHome'
import EnvHome from './components/fragment/environment/EnvHome'
import InfoHome from './components/fragment/information/InfoHome'
import NewsHome from './components/fragment/information/news/NewsHome'
import NewJokes from './components/fragment/information/joke/NewJoke'
import BooksHome from './components/fragment/information/books/BooksHome'
import WeChatHome from './components/fragment/information/wechatnews/WeChatNewsHome'
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
      },
      {
        name:'jokes',
        path:'jokes/',
        component:NewJokes
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
