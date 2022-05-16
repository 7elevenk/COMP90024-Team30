import tweepy
import json
import couchdb
import random

#consumer_key = "DTly4o4Y0YTmIcdmgRDVn8vdV"
#consumer_secert = "ecbfjzyexcUZrLRzCPQfopqh3d4lxUa2xtyFNDMxkQ39CPqg5H"
#access_secert = "Ns6arxrgtUJSg2XscXmFZhaghipF2ppYHwuv4jt9iimQW"
#access_token = "1450746865272508417-xwj2SIv4GQ7662m9YTOThKzLmcCDKf"
#bearer_token='AAAAAAAAAAAAAAAAAAAAAJHZcQEAAAAA112E9e8F3VU0kFTMv8QqCAxlRWQ%3DaU3BP4vxTEFOWl8gYOZax2X8ieSRG0vLw3zDQtgHWTUWOOFExd'

consumer_key='U0Ey849XAKpp21R8jKxhXph5r'
consumer_secert='GiN8wTm2pr6jY47euvWiDWkYCWFxzxLYVsxEiuK7g6OFZPHZBo'
bearer_token='AAAAAAAAAAAAAAAAAAAAAKDvbQEAAAAANoYB2togoGyyHIGMVys%2BU6TYQQk%3DYu8DpCWPBq0AVUBkS1HmgJvjXWMQLRcKBFl2PbaSZSnxzyjUWO'
access_token='1514519574380957698-CCzsE52Zc62oA5Z8xTRvcSuz8HGHWP'
access_secert='dUoXzTB9F9aC0kCvGkOFTtereeIcFCMVXhpD93rxUSu0c'

couch = couchdb.Server("http://admin:admin@172.26.131.153:5984")


db_name = "mel_tweets"

if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

auth = tweepy.OAuthHandler(consumer_key, consumer_secert)
auth.set_access_token(access_token,access_secert)
api = tweepy.API(auth)

client = tweepy.Client(bearer_token=bearer_token)
# ids of the offical melb twitter account
idnum_list = ["223282435", "43064490", "240421228","844691982639251456"]
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
