from  pymongo import MongoClient
import requests
from api import APP_API
import json

class DataInit():
    client = MongoClient('localhost', 27017)
    #softwork db
    db = client['SoftWork']
    user_col = db['user_data']
    merchant_col = db['merchant_data']
    city_col = db['city_data']
    station_col = db['station_data']
    books_col = db['books_data']

    def userAdd(self):
        user_dict = {
            "basic":
            {'name': 'abc',
             'password': '123',
             'sex':'男'
             }
        }
        self.user_col.insert_one(user_dict)
        for i in self.user_col.find():

            print(i)

    def getuser(self): #get recent user data
        return self.user_col.find_one()

    def checkuser(self,**arg):
        check = self.user_col.find(arg)
        if check:
            return True
        return False
    def addinfo(self):

        # self.merchant_col.insert_one(
        #
        # )
        # with open('../data/data.json','r') as f:
        #     print(f.read()["info"])
            # self.merchant_col.insert_one(f.read())
        for i in self.merchant_col.find():
            print(i)
    def add_city(self):
        a = requests.get(APP_API["weather"]['cities'], params={'key': APP_API['weather']['key']})
        DataInit.city_col.insert_one(a.json())

    def add_station(self):
        DataInit.station_col.insert_one(requests.get(APP_API["water"]['stations'], params={'key': APP_API['water']['key']}).json())

    def add_books(self):
        DataInit.books_col.insert_one(requests.get(APP_API["books"]['getBooks'], params={'key': APP_API['books']['key']}).json())

    class SportInit(object):

        def __init__(self):
            self.out = DataInit()
            self.team_col = self.out.db['team_data']

        def add_team(self):
            teams = requests.get(APP_API['sport']['basketball']['getTeam'], params={'key':APP_API['sport']['basketball']['key']}).json()
            self.team_col.insert_one(teams)




    def __init__(self):
        #self.userAdd()
        pass


if __name__ == '__main__':
    data_init = DataInit()
    spot_init = data_init.SportInit()
    # cities = data_init.city_col.find_one()
    # print(cities)
    #data_init.add_city()
    #data_init.add_station()
    #data_init.add_books()
    spot_init.add_team()



