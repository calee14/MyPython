# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '929046961507917824-dbwwmnpldvwCYhR1XkbR6cgfJonCKhV'
ACCESS_SECRET = 'PsweQOWstsT6yuJLWLUFQZe3ulhiCRNAwzOH9mh1cyaAY'
CONSUMER_KEY = 'R7OiC7iR7fnJUW6TUGV9nFjly'
CONSUMER_SECRET = '2zpC2Kf3ynWXYTQ0WDNyfoKhYS10NYOn6UglLG0zWkr9fB5mqX'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
#twitter_stream = TwitterStream(auth=oauth)

# If we need to use other streams to collect data
twitter_stream = TwitterStream(auth=oauth, domain='userstream.twitter.com')

# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()

# Get tweets in English that include the term 'Google'
iterator = twitter_stream.statuses.filter(track="Google", language="en")

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 