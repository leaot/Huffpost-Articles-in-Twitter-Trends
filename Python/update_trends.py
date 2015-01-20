# This file used to update trends in database.
import tweepy
import pymongo
import json
from pymongo import MongoClient



def get_trends_place(place_id):
    auth = tweepy.OAuthHandler("QOgmguBKBSRMKIvsKSnQHKtRh", "Q1b2qx1jmqmyz1W1MQybKxVFjT2Xki4I09nIaopWRttNcUzagb")
    auth.set_access_token("830970282-3m0aLd06DIC9Yp5M3koaSbDyNFAeiAqLhqRZi7Qs", "MAKSvwoIqfnO9KIxdBVJQUdKwJYRrZWaT3aEafXpQzjoj")
    api = tweepy.API(auth)
    return api.trends_place(place_id)

def update_to_db(trends_data):
    # database connection
    try:
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.lyl
        db.trends.drop()   # need to change back to trends!!!!!
        db.trends.insert(trends_data)

    except Exception,e:
        print "LYL:Pymongo connection error:\n",str(e)

trends = get_trends_place(2459115)  
jsondata =json.dumps(trends) 
update_to_db(trends)

print jsondata