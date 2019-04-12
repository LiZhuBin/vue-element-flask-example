# coding=utf-8

import requests
from flask import render_template, Flask, request, jsonify, make_response, Blueprint

from myapp.api import APP_API
from myapp.datadeal.dataDeal.dataInit import DataInit
import json
weather_blue = Blueprint("weather", __name__, url_prefix="/home/weather")
water_blue = Blueprint("water", __name__, url_prefix="/home/water")
news_blue = Blueprint("news", __name__, url_prefix="/home/info/news")
books_blue = Blueprint('books', __name__, url_prefix='/home/info/books')
wechat_blue = Blueprint('wechatNews', __name__, url_prefix='/home/info/weChatNews')
sport_blue = Blueprint('sport', __name__, url_prefix='/home/sport')
joke_blue = Blueprint('joke', __name__, url_prefix='/home/info/jokes')

app = Flask(__name__)

data_init = DataInit()


@app.after_request
def af_request(resp):
    """
    #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


@app.route('/', methods=['GET', 'POST'])
def a():
    return jsonify({'results': "fff"})


@app.route('/login/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        user_data = data_init.getuser()
        name = user_data['cities_dataasic']['name']
        password = user_data['cities_dataasic']['password']
        return jsonify({'name': name, 'password': password})
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

    return 'name:{}'.format("fdddddddddddf")


@weather_blue.route('/getcity', methods=['GET'])
def get_city():
    """:return city list"""
    cities = DataInit.city_col.find_one()['result']
    cities_data = {}
    for city in cities:
        if city['city'] in cities_data:
            cities_data[city['city']].append({'value': city['district'], 'label': city['district']})
        else:
            cities_data[city['city']] = []
            cities_data[city['city']].append({'value': city['district'], 'label': city['district']})
    d = [{'value': i, 'label': i, 'children': j} for i, j in cities_data.items()]

    return jsonify(d)

@water_blue.route('/getstation', methods=['GET'])
def get_station():
    stations = DataInit.station_col.find_one()['result']

    return jsonify( [{'value':station ,'label':station }for station in stations])

@weather_blue.route('/getweather/usecity', methods=['GET', 'POST'])
def by_city():
    city = request.args.get('city')

    weathers = requests.get(APP_API["weather"]['weatherByCity'], params={'key': APP_API['weather']['key'], 'city': city}).json()[
        'result']
    # weather_return = weathers['realtime']
    # weather_return['city'] = weathers['city']
    return jsonify(weathers)

@water_blue.route('/getstation/usestation', methods=['GET', 'POST'])
def by_station():
    state = request.args.get('state')

    water = requests.get(APP_API["water"]['waterByStation'], params={'key':APP_API['water']['key'],'state': state}).json()
    return jsonify(water)

@news_blue.route('/getnews/<type>', methods=['GET', 'POST'])
def by_station(type):

    water = requests.get(APP_API["news"]['getNews'], params={'key':APP_API['news']['key'],'type': type}).json()
    return jsonify(water)

@books_blue.route('/getBooksType', methods=['GET', 'POST'])
def get_books_type():
    books = DataInit.books_col.find_one()['result']
    return jsonify(books)

@books_blue.route('/getBooksContent/<id>')
def get_books_content(id):
    content = requests.get(APP_API['books']['getContent'],params={'key':APP_API['books']['key'],'catalog_id':id}).json()

    return jsonify(content)

@wechat_blue.route('/getBooksContent/<ps>/<pno>')
def get_wechat_content(ps,pno):
    content = requests.get(APP_API['wechat']['getContent'], params={'key':APP_API['wechat']['key'],'pno':pno,'ps':ps}).json()
    return jsonify(content)

@sport_blue.route('/basketball/getTeamName')
def get_team_name():
    contents = DataInit.SportInit().team_col.find_one()
    names = [{'id': key, 'name': content['full_name']} for (key, content) in contents['result'].items()]
    return jsonify(names)

@sport_blue.route('/basketball/getTeam/<id>')
def get_team_data(id):
    contents = DataInit.SportInit().team_col.find_one()['result'][id]
    return jsonify(contents)

@joke_blue.route('/getNewJoke/',methods=['GET', 'POST'])
def get_jock_new():
    content = ''
    id = request.args.get('id')
    page = request.args.get('page')
    pagesize = request.args.get('pagesize')

    if id == '1':

        content = requests.get(APP_API['joke']['new']['getNew'],params={'key':APP_API['joke']['new']['key'],'page':page,'pagesize':pagesize}).json()
    else :
        content = 'ffdd'
    return jsonify(content)
@joke_blue.route('/getRandomJoke/')
def get_joke_random():
    return jsonify(requests.get(APP_API['joke']['random']['getRandom'],
                        params={'key':APP_API['joke']['random']['key'],
                                }).json())






if __name__ == '__main__':

    app.register_blueprint(weather_blue)
    app.register_blueprint(water_blue)
    app.register_blueprint(news_blue)
    app.register_blueprint(books_blue)
    app.register_blueprint(wechat_blue)
    app.register_blueprint(sport_blue)
    app.register_blueprint(joke_blue)
    app.run()
