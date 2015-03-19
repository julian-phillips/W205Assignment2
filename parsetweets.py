# -*- coding: utf-8 -*-
import json
import re
import tinys3
import csv
conn = tinys3.Connection('XXX', 'XXX')
bucket = ('jp.mids.assignment2')
tweetlist = {}

jsontweets = open("tweets.txt", "r")
chunktweets = []
for tweet in jsontweets:
    tweet = json.loads(tweet)  
    if tweet["lang"] <> 'en':            
        continue
    else:
        chunktweets.append(tweet)
        sentence= tweet["text"]     
        sentence_noURL= re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', sentence)
        sentence_noURL= re.sub('[-!?,";:&]+', '', sentence_noURL)
        sentence_noURL=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",sentence_noURL)
        sentence_noURL=re.sub("RT","",sentence_noURL).lower()
        words = sentence_noURL.split()
        for word in words:
            if word in tweetlist:
                tweetlist[word] +=1
            else:
                tweetlist[word] =1


w = csv.writer(open("output.csv", "w"))
for key, val in tweetlist.items():
    w.writerow([key, val])

q = csv.writer(open("chunktweets.csv", "w"))
for val in chunktweets:
    q.writerow([val])



f=open("output.csv",'rb')
g=open("chunktweets.csv",'rb')
conn.upload("output.csv",f,bucket)
conn.upload("chunktweets.csv",g,bucket)