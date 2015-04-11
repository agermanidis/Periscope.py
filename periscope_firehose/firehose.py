import tweepy
from utils import get_periscope_url_from_tweet, get_stream_info
from broadcast import PeriscopeBroadcast

def tweet_to_broadcast(status):
    try:
        web_url = get_periscope_url_from_tweet(status)
        info = get_stream_info(web_url)
        broadcast = PeriscopeBroadcast(info['data'],
                                       web_url = web_url,
                                       token_id = info["token_id"])
        return broadcast
    except:
        pass

class PeriscopeFirehose(object):
    class PeriscopeTweetListener(tweepy.StreamListener):
        def on_status(self, status):
            broadcast = tweet_to_broadcast(status)
            if not broadcast: return
            self.subscriber.on_broadcast(broadcast)
    
    def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(oauth_token, oauth_secret)
        self.api = tweepy.API(self.auth)
        self.listener = PeriscopeFirehose.PeriscopeTweetListener()
        self.listener.subscriber = self
        self.stream = tweepy.Stream(self.auth, self.listener, timeout = None)
        
    def listen(self):
        self.stream.filter(track=['#Periscope'])

    def get_most_recent_broadcasts(self, limit = 100, only_running = False):
        results = self.api.search("#Periscope", limit = 100)
        broadcasts = map(tweet_to_broadcast, results)
        broadcasts = filter(lambda b: b is not None, broadcasts)
        if only_running:
            broadcasts = filter(lambda b: b.is_running(), broadcasts)
        return broadcasts

    def on_broadcast(self, broadcast):
        # override this
        pass
    
