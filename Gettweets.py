import tweepy;
import json;


import tinys3



-consumer_key = 'XXX';
-consumer_secret = 'XXX';
+consumer_key = "XXX";
+consumer_secret = "XXX";

conn = tinys3.Connection('XXX', 'XXX')

bucket = ('jp.mids.assignment2')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth,wait_on_rate_limit=True) 
tweets= tweepy.Cursor(api.search, q = "#microsoft OR #mojang", since = "2015-03-30", until = "2015-04-01").items()


with open("tweets_1.txt", "w") as file:
    tweetct = 0
    totalct = 0
    while True:        
        try:            
            tweet = tweets.next()    
            json.dump((tweet._json),file,encoding="utf-8")
            file.write('\n')
            tweetct +=1
            if tweetct ==20000:
                tweetct = 0
                totalct+=1
                file.close()
                file = open("tweets_"+str(totalct)+".txt","w")
        except StopIteration:
            break
        
        
file.close() 
f=open("tweets.txt",'rb')
