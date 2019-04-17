import axios from 'axios'
export const getNews = data =>{
  return axios({
    url: this.GLOBAL.URL_NEWS + 'getnews/',
    method: 'get',
    data
  })
}
