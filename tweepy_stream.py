import tweepy
from config import APIConfig

class BitcoinStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)

    def on_error(self, status):
        print(status)

apiConfig = APIConfig()
auth = apiConfig.createAuth()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth, myStreamListener)
myStream.filter(track=['bitcoin'])