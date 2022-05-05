import os
from tweepy import Client
import tweepy
import pandas as pd

consumer_key = "consumer_key"
consumer_secert = "consumer_secert"
access_secert = "access_secert"
access_token = "access_token"
bearer_token='bearer_token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secert)
auth.set_access_token(access_token,access_secert)
api = tweepy.API(auth)

number_of_tweets = 800
tweets = []

for i in tweepy.Cursor(api.search_tweets, q='#auspol', tweet_mode='extended').items(number_of_tweets):
    tweets.append(i._json)
    
"""
Creative one
client = tweepy.Client(bearer_token=bearer_token)
idnum = '223282435' # id of the offical melb twitter account
#max_count = 50
#count = 0
number_of_tweets = 50
tweets = []

users = client.get_users_following(id=idnum,max_results=10)
for user in users.data:    
    print(user.id)
    for i in tweepy.Cursor(api.user_timeline, id=user.id, tweet_mode="extended").items(number_of_tweets):
        tweets.append(i._json)
    
"""

print(tweets)

