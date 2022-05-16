import tweepy
import json
import couchdb
import random

consumer_key = "rvQxwxxk4OABaJOunbwG6WU3e"
consumer_secert = "UTRt8VTsMDKRBSfwZ8GTctcoHTnSkm215pfELtwCZk608awPr1"
access_secert = "iY156efuUfHpF7b8R8DNYn6X84UWpqE2jzgUHvBFPLasT"
access_token = "4834166883-YHCL7QiHCDWxa9rKPpz4D43n2uEW5DGaTqFha01"
bearer_token="AAAAAAAAAAAAAAAAAAAAAK4QbgEAAAAAZjbJ4cohGtBlzh5ozYIJ7vpXkSw%3DzXbZQC7D8TTiiohApxEDg7wTLShLXxpiHOa3p92LNEMixvWYOO"

couch = couchdb.Server("http://admin:admin@172.26.131.153:5984")


db_name = "syd_tweets"

if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

auth = tweepy.OAuthHandler(consumer_key, consumer_secert)
auth.set_access_token(access_token,access_secert)
api = tweepy.API(auth)

client = tweepy.Client(bearer_token=bearer_token)
# ids of the offical sydn twitter account
idnum_list = ["23546978", "40778270", "17180384", "436226316"]
randomint = random.randint(0,3)
number_of_tweets = 50

users = client.get_users_following(id=idnum_list[randomint],max_results=100)
for user in users.data:    
    for i in tweepy.Cursor(api.user_timeline, id=user.id, tweet_mode="extended").items(number_of_tweets):
        #tweet1 = str(i._json).replace("\'", "\"")
        #tw = tw.replace("False", "\"False\"")
        #tweet2 = json.dumps(tweet1)
        #db_entry = json.loads(tweet2)
        tweet=json.dumps(i._json)
        db_entry = json.loads(tweet)
        doc_id = db_entry["id"]
        if str(doc_id) not in db:  
            db[str(doc_id)] = {"tweet": db_entry}
