# -*- coding: utf-8 -*-
import csv
import re
import tinys3
conn = tinys3.Connection('XXX', 'XXX')
bucket = ('jp.mids.assignment2')
tweetlist = {}

with open("tweets.txt", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for line in reader:
        if line[1] <> 'en':            
            continue
        else:
            sentence= line[0]     
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

f=open("output.csv",'rb')
conn.upload("output.csv",f,bucket)