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

def retrieve_id(file):
    ids = []
    with open(file, 'r') as f:
        for i in range(len(f)):
            if '\n' in f[i]:
                ids.append(f[i][:-1].strip())
            else:
                ids.append(f[i].strip())
    return ids

def store_id(id, file):
    with open(file, 'a') as f:
        f.write(str(id) + '\n')
    return

