import os
from dotenv import load_dotenv
import tweepy
import time
import states_dist
import spreadsheet
from locApi import loc

load_dotenv()

google_map = loc()  # Object of loc class

services = ['oxygen', 'beds', 'bed']    # List of services available

token = os.getenv("TOKEN")                       # API Key-Tokens
token_secret = os.getenv("TOKEN_SECRET")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)       # Connecting to bot using creds
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)

def retrieve_id(file_name):
    '''
    Function to retrieve tweet id from file
    and save it in a list of ids.
    '''

    ids = []
    with open(file_name, 'r') as file:
        f = file.readlines()
        for i in range(len(f)):
            if '\n' in f[i]:
                ids.append(f[i][:-1].strip())
            else:
                ids.append(f[i].strip())
    return ids

def store_id(id, file_name):
    '''
    Function to store tweet key into file.
    '''

    with open(file_name, 'a') as f:
        f.write(str(id) + '\n')
    return

def scrape(hashtag, date_since):
    
    tweets = tweepy.Cursor(api.search, q=hashtag, lang="en", since=date_since, tweet_mode='extended').items()

    tweets_list = [tweet for tweet in tweets]

    for tweet in reversed(tweets_list):
        id = tweet.id_str

        ids = retrieve_id('lastseen_id.txt')

        if id not in ids:
            text = tweet.full_text

            state = find_state(text.lower())
            service = find_service(text.lower(), service.lower())

            print(str(id) + ' - ' + text, flush=True)

            tweet_toSend = spreadsheet.get_tweet(state)

            api.update_status('@' + tweet.user.screen_name + " " + tweet_toSend, id)
            store_id(id, 'lastseen_id.txt')
        else:
            print("Already replied to " + str(id))

#states = states_dist.get_states()

"""
def find_state(tweet):
    tweet = tweet.title()
    print(tweet)
    print(type(tweet))

    for state in states:
        for dist in states[state]:
            if dist in tweet:
                if state == None:
                    print("GOT THIS !!")
                else:
                    return state
"""

def find_state(tweet):
    '''
    Find state from tweet
    Iterate through tweet words and put them in google map API
    fetch the state and return it.
    '''

    tweet_list = tweet.split()

    for t in tweet_list:
        address = google_map.locate(t)
        display_name = address['display_name'].split(',')
        country = display_name[-1].strip()
        state = display_name[-2].strip()

        if country == "India":
            try:
                temp = int(state)
                state = display_name[-3].strip()
                return state
            except ValueError:
                return state

def find_service(tweet):
    '''
    Find the service need from user's tweet
    '''
    tweet_list = tweet.split()

    for t in tweet_list:
        if t in services:
            return t


while True:
    scrape("#covidwarriorbottesting", "2021-05-13")
    time.sleep(10)