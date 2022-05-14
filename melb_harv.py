import tweepy
import json
import couchdb

consumer_key = "U0Ey849XAKpp21R8jKxhXph5r"
consumer_secert = "GiN8wTm2pr6jY47euvWiDWkYCWFxzxLYVsxEiuK7g6OFZPHZBo"
access_secert = "dUoXzTB9F9aC0kCvGkOFTtereeIcFCMVXhpD93rxUSu0c"
access_token = "1514519574380957698-CCzsE52Zc62oA5Z8xTRvcSuz8HGHWP"
bearer_token='AAAAAAAAAAAAAAAAAAAAAKDvbQEAAAAANoYB2togoGyyHIGMVys%2BU6TYQQk%3DYu8DpCWPBq0AVUBkS1HmgJvjXWMQLRcKBFl2PbaSZSnxzyjUWO'

couch = couchdb.Server("http://admin:admin@172.26.131.153:5984")
db = couch["melb_tweets"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secert)
auth.set_access_token(access_token,access_secert)
api = tweepy.API(auth)

client = tweepy.Client(bearer_token=bearer_token)
idnum = '223282435' # id of the offical melb twitter account

number_of_tweets = 100

users = client.get_users_following(id=idnum,max_results=50)
for user in users.data:    
    for i in tweepy.Cursor(api.user_timeline, id=user.id, tweet_mode="extended").items(number_of_tweets):
        #tweet1 = str(i._json).replace("\'", "\"")
        #tw = tw.replace("False", "\"False\"")
        #tweet2 = json.dumps(tweet1)
        #db_entry = json.loads(tweet2)
        tweet=json.dumps(i._json)
        db_entry = json.loads(tweet)
        db.save(db_entry)
