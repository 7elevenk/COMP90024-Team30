import tweepy
import json
import couchdb
import random

consumer_key = "U0Ey849XAKpp21R8jKxhXph5r"
consumer_secert = "GiN8wTm2pr6jY47euvWiDWkYCWFxzxLYVsxEiuK7g6OFZPHZBo"
access_secert = "dUoXzTB9F9aC0kCvGkOFTtereeIcFCMVXhpD93rxUSu0c"
access_token = "1514519574380957698-CCzsE52Zc62oA5Z8xTRvcSuz8HGHWP"
bearer_token='AAAAAAAAAAAAAAAAAAAAAKDvbQEAAAAANoYB2togoGyyHIGMVys%2BU6TYQQk%3DYu8DpCWPBq0AVUBkS1HmgJvjXWMQLRcKBFl2PbaSZSnxzyjUWO'

couch = couchdb.Server("http://admin:admin@172.26.131.153:5984")

db_name = "bne_tweets"
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

auth = tweepy.OAuthHandler(consumer_key, consumer_secert)
auth.set_access_token(access_token,access_secert)
api = tweepy.API(auth)

client = tweepy.Client(bearer_token=bearer_token)
# ids of the offical bne twitter account
idnum_list = ["41312733", "43040214", "35997368", "275294751", "256833444"]
randomint = random.randint(0,4)
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
