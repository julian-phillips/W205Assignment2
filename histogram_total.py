import numpy as np
import pylab as pl
import tinys3
conn = tinys3.Connection('AKIAIUWDSESWGVSNDSCA', '5hQetAaRQ/3jDA+s6NrUwScK1CICJnJjVJdLqfoB')

bucket = ('jp.mids.assignment2')
dic = {}
#Load the text file as a key, value dictionary

with open("output.csv") as sourceFile:
    for line in sourceFile:
        (val, key) = line.split(',')                
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
pl.savefig('totalplot.png')

f=open('totalplot.png','rb')
conn.upload('totalplot.png',f,bucket)
