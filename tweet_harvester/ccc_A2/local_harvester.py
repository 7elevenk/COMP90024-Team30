import tweepy
import json
import io

consumer_key = "QTJlIyomXlNZvuLI16rSOGjIE"
consumer_secret = "OzKgI2RUEupu2D64cq64aHkfZymboS0ZhnglUQeQ8MbwwrkgnI"
access_token = "1511905209487749134-53Z8zNTXLK9NCEnhTaIXFW3upQNibx"
access_token_secret = "XTlRGA1ov1tOgaOr3dUXgSNPLQmkmVspLLL33vDlCIOE7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print(api)

# key hashtag
search_term = "#melbourne"

# create a new file
file_name = "tweets.json"
target_file = io.open(file_name, 'a', encoding='utf-8')

# get random 800 tweets with our key hashtag
search = tweepy.Cursor(api.search_tweets, q=search_term, lang="en").items(800)
search_tweet = [status._json for status in search]
json_str = [json.dumps(json_obj) for json_obj in search_tweet]

# write 800 tweets in file and encoding to utf-8 format
target_file = open("tweets.json", "w", encoding='utf-8')
json.dump(json_str, target_file, ensure_ascii=False, indent=4)
target_file.close()
