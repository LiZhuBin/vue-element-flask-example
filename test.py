import requests

from myapp.api import APP_API

weathers= requests.get(APP_API["weather"]['weatherByCity'], params={'key': APP_API['key'],'city':'上海'}).json()['result']
items = ['city','temperature','humidity','info','wid','direct','power','aqi']
weather_return = weathers['realtime']
weather_return['city'] = weathers['city']


#weather_return = [{item:weather[item]}for item in items for weather in weathers['result']['realtime']]
print(weather_return)