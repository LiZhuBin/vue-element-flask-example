APP_API = {

    "weather":{
        'key':"b52d4d4bc835f35a03ed2725a1db0d23",
        "cities": "http://apis.juhe.cn/simpleWeather/cityList",
        'weatherByCity':"http://apis.juhe.cn/simpleWeather/query",
    },
    "water":{
        'key':'8557f89fb7f3280c9ce9be92e9a6a94d',
        'stations': 'http://web.juhe.cn:8080/environment/water/stateList',
        'waterByStation':'http://web.juhe.cn:8080/environment/water/state'
    },
    'news':{
        'key':'6ca85b5af9dde4519e58d4fd8997eb05',
        'getNews':'http://v.juhe.cn/toutiao/index',
    },
    'books':{
        'key':'e7a991e53ec3a0675d065c0bb90ab8de',
        'getBooks':'http://apis.juhe.cn/goodbook/catalog',
        'getContent':'http://apis.juhe.cn/goodbook/query'
    },
    'wechat':{
        'key':'bcb4dbea21618741efa56a4a8ab09d15',
        'getContent':'http://v.juhe.cn/weixin/query'
    }

}