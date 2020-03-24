
# web_app/services/twitter_service.py

import os
from dotenv import load_dotenv
import tweepy
from pprint import pprint

load_dotenv()
consumer_key = os.getenv("TWITTER_API_KEY", default="OOPS")
consumer_secret = os.getenv("TWITTER_API_SECRET", default="OOPS")
access_token = os.getenv("TWITTER_ACCESS_TOKEN", default="OOPS")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", default="OOPS")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
print("AUTH", type(auth))

api = tweepy.API(auth)
print("API", type(api)) #> <class 'tweepy.api.API'>
#breakpoint()

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

# get information about a twitter user:
screen_name = "elonmusk"
print("--------------")
print("USER...")

user = api.get_user(screen_name)
print(type(user)) #> <class 'tweepy.models.User'>
print(user.screen_name)
print(user.followers_count)

pprint(user._json)
print("--------------")
print("STATUSES...")

# get that user's tweets:
# see: http://docs.tweepy.org/en/latest/api.html#API.user_timeline
statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
for status in statuses:
    print(type(status)) #> <class 'tweepy.models.Status'>
    #pprint(status._json)
    #breakpoint()
    print(status.full_text)