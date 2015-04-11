# The Periscope Firehose!

This library provides an easy way to listen for new Periscope streams published on Twitter.

### Usage

```python
from periscope_firehose import PeriscopeFirehose

class MyFirehose(PeriscopeFirehose):
    def on_broadcast(self, broadcast):
        print "New Periscope Broadcast published!"
        print "- id:", broadcast.id
        print "- twitter handle:", broadcast.twitter_screen_name
        print "- status:", broadcast.status

firehose = MyFirehose(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_OAUTH_TOKEN, TWITTER_OAUTH_SECRET)
firehose.listen()
```

Get your Twitter consumer key, consumer secret, oauth token, and oauth secret from the [Twitter Application Management page](https://apps.twitter.com/).