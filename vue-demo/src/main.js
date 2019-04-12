import Vue from 'vue'
import App from './App.vue'
import Home from './components/Main.vue'
import VueRouter  from 'vue-router';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import global_ from './Global.vue'
import qs from 'qs'
import routers from './routers'
import axios from 'axios'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
// axios 配置
axios.defaults.timeout = 8000;
axios.defaults.baseURL = global_.URL_ROOT;


Vue.prototype.$http = axios;

Vue.prototype.qs = qs;
Vue.config.productionTip = false;

Vue.prototype.GLOBAL = global_;

Vue.use(ElementUI);
Vue.use(VueRouter);


const router = new VueRouter({
  mode: 'history',
  routes: routers
});

const app = new Vue({
  name: '#app',
    router,
    render: h => h(Home)
}).$mount('#app');



