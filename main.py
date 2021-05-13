import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

token = os.getenv("TOKEN")
token_secret = os.getenv("TOKEN_SECRET")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)
