### W205Assignment2
I used three python files to complete the assignment, although they could be combined into one.

1) Gettweets.py
2) Parsetweets.py
3) Histogram.py (two variants, one for a complete histogram one for a limited one)

S3 bucket: jp.mids.assignment2

Limitedplot.png only shows words that had a frequency of over 500 while totalplot.png shows all.
###Revisions

Per your comments:

The missing items are:

No partition of raw tweets (Jsons) - Entire JSONs are now saved.

No set of tweets organization on S3 (tweet’s text chunking ) - Within parsetweets, the tweets are chunked and saved on S3 seperately.

No resiliency in the code (rate limit, intrupt,…) - The twitter API rate limit handler is now used.


