#import module
import re
from operator import add
from pyspark import SparkContext, SparkConf  
conf = SparkConf().setAppName("WordCount").setMaster('local')  
sc = SparkContext(conf=conf)  
#read input file
file_in = sc.textFile('/home/xhades/spark/README.md')

#count lines
print 'number of lines in file: %s' % file_in.count()

#add up lenths of each line
chars = file_in.map(lambda s: len(s)).reduce(add)
print 'number of cjaracters in file: %s' % chars

#get words from the input file
words = file_in.flatMap(lambda line: re.split('\W+',line.lower().strip()))

#words of more than 3 characters
words = words.filter(lambda x: len(x) > 3)

#set count 1 per word 
words = words.map(lambda w: (w,1))

#reduce phase - sum count all the words 
words = words.reduceByKey(add)

#create tuple (count,words) and sort in descending
words = words.map(lambda x: (x[1],x[0])).sortByKey(False)
print words.take(10)


#create function for histogram of most frequent words
import matplotlib.pyplot as plt
#plt.figure(figsize=(8,6))

def histogram(words):
    count = map(lambda x: x[1], words)
    word = map(lambda x: x[0], words)
    plt.barh(range(len(count)), count,color = 'grey')
    plt.yticks(range(len(count)), word)
    plt.show()

# display histogram
histogram(words.take(10))