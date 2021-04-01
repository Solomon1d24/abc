import tweepy
import time
consumer_key = 'PpZFbvn4DZYos7zMptVZSUftt'
consumer_secret = '3yvRxsOG01XwkKPK4s2qyFDgRBapzeqiAUgWWuekXWCNb8mRhF'
access_token = '337121648-N81bYq9przAfczcZ3uRKDwnPS2gFhvfAKAjNHvXX'
access_token_secret = '7OEgTVt8yCrfbpj2O7XhPWsdTmtRvlsj97osJCsfO7CR2'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

#Generousbot
for followers in limit_handle(tweepy.Cursor(api.followers).items()):
    followers.follow()
