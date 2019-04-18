import Main from './components/Main.vue'
import Login from './components/main/user/Login'
import SignOut from './components/main/user/SignOut'
import Bycity from './components/main/environment/weather/WeatherHome'
import ByStation from './components/main/environment/water/WaterHome'
import EnvHome from './components/main/environment/EnvHome'
import InfoHome from './components/main/information/InfoHome'
import NewsHome from './components/main/information/news/NewsHome'
import NewJokes from './components/main/information/joke/NewJoke'
import RandomJokes from './components/main/information/joke/RandomJoke'
import BooksHome from './components/main/information/books/BooksHome'
import WeChatHome from './components/main/information/wechatnews/WeChatNewsHome'
import SportHome from './components/main/sport/SportHome'
import BasketBallHome from './components/main/sport/basketball/BasketBallHome'
import TeamView from './components/main/sport/basketball/TeamView'
import InfoMain from './components/main/information/InfoMain'

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
    children: [
      {
        name: 'InfoMain',
        path: '/',
        component: InfoMain
      },
      {
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
        name: 'jokes',
        path: 'jokes/',
        component: NewJokes
      },
      {
        name: 'randomJokes',
        path: 'jokes/randomJokes/',
        component: RandomJokes
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
    path: '/user/',
    component: Login,
    children:[{
      path:'signin',
      component: Login,
    },
        {
    path: 'signout',
    name: SignOut,
    component: SignOut
  }
    ]
  },



];
export default routers
