import tweepy;
import json;
import time;

import tinys3



consumer_key = 'XXX';
consumer_secret = 'XXX';

access_token = 'XXX';
access_token_secret = 'XXX';

conn = tinys3.Connection('XXX', 'XXX')

bucket = ('jp.mids.assignment2')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
tweets= tweepy.Cursor(api.search, q = "#microsoft OR #mojang", since = "2015-02-03", until = "2015-02-10").items()


with open("tweets.txt", "w") as file:
    while True:
        try:
            tweet = tweets.next()    
            json.dump((tweet._json['text'].replace('\n',' ').encode('ascii', 'ignore'),tweet._json['lang'],tweet._json['created_at']),file,separators=('|', ': '),encoding="utf-8")
            file.write('\n')
        except tweepy.TweepError:
            time.sleep(900)
            continue
        except StopIteration:
            break
        
        
file.close() 
f=open("tweets.txt",'rb')
conn.upload("tweets.txt",f,bucket)