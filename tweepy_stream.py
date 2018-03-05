import tweepy
from config import APIConfig

class BitcoinStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)

    def on_error(self, status):
        print(status)

apiConfig = APIConfig()
auth = apiConfig.createAuth()

btcStreamListener = BitcoinStreamListener()
stream = tweepy.Stream(auth, btcStreamListener)
stream.filter(track=['bitcoin'])