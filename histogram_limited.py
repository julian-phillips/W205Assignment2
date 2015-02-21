import numpy as np
import pylab as pl
import tinys3
conn = tinys3.Connection('XXX', 'XXX')

bucket = ('jp.mids.assignment2')
dic = {}
#Load the text file as a key, value dictionary

with open("output.csv") as sourceFile:
    for line in sourceFile:
        (val, key) = line.split(',')
        if int(key) < 500:
            continue
        else:            
            dic[int(key)] = val
 
    
#Seting the number of bins, Axes values        
X = np.arange(len(dic))
pl.bar(X, dic.keys(), width=0.2)
pl.xticks(X, dic.values())

#Setting the axis range
ymax = max(dic.keys()) + 1
pl.ylim(0, ymax)

#ploting the histogram
pl.show()
pl.savefig('limitedplot.png')

f=open('limitedplot.png','rb')
conn.upload('limitedplot.png',f,bucket)
