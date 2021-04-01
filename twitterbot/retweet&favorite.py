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
            yield cursor
    except tweepy.RateLimitError:
        time.sleep(300)

search_string = 'python'
numberofTweets = 2

for tweet in tweepy.Cursor(api.search,search_string).items(numberofTweets):
    try:
        tweet.retweet()
        print('I like that Tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopAsyncIteration:
        break