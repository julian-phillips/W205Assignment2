import tweepy;
import json;


import tinys3



consumer_key = "XXX";
consumer_secret = "XXX";

access_token = "XXX";
access_token_secret = "XXX";


conn = tinys3.Connection("XXX", "XXX")

bucket = ('jp.mids.assignment2')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth,wait_on_rate_limit=True) 
tweets= tweepy.Cursor(api.search, q = "#microsoft OR #mojang", since = "2015-03-06", until = "2015-3-16").items()


with open("tweets.txt", "w") as file:
    while True:
        try:
            tweet = tweets.next()    
            json.dump((tweet._json),file,encoding="utf-8")
            file.write('\n')        
        except StopIteration:
            break
        
        
file.close() 
f=open("tweets.txt",'rb')
conn.upload("tweets.txt",f,bucket)