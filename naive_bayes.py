from __future__ import division
import nltk
from nltk.tokenize import word_tokenize
import parse
import operator
from nltk.corpus import wordnet as wn
import math

(ratings, sentiments, sent_list)= parse.parse('train/ScottRenshaw_train.txt')
leg={"d":0,"c-":1,"c":2,"c+":3, "b-":4,"b-":5,"b+":6,"a-":7,"a":8,"a+":9}
TOT={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0, "sum":0}
def train(ratings, sentiments):
    data={}
    for RID, sents in sentiments.iteritems():
        TOT[int(ratings[RID])]=TOT[int(ratings[RID])]+1
        TOT["sum"]=TOT["sum"]+1
        data[RID]={"score":int(ratings[RID]),-2:0,-1:0,0:0,1:0,2:0}
        for k in sents:
            val=k[1]
            data[RID][val]=data[RID][val]+1
    return data

def average(s):
    if len(s)==0:
        return 0
    else:
        return sum(s) * 1.0 / len(s)
def stdev(s, avg):
    if avg==0:
        return 1/10
    else:
        variance = map(lambda x: (x - avg)**2, s)
        return math.sqrt(average(variance))

def stat(data):
    count={}
    scores=[0,1,2,3,4,5,6,7,8,9,10]
    values=[-2,-1,0,1,2]
    for s in scores:
        count[s]={}
        for v in values:
            count[s][v]={"all":[],"mean":0,"sd":0};
    for key, value in data.iteritems():
        sc=value['score']
        for i in [-2,-1,0,1,2]:
            count[sc][i]["all"].append(value[i])
    for s in scores:
        for v in values:
            curr=count[s][v]["all"]
            count[s][v]["mean"]=average(curr)
            count[s][v]["sd"]=stdev(curr,count[s][v]["mean"])
    return count

def normpdf(x, mean, sd):
    if mean==0:
        return .00000000000000000000000000000000001
    var = float(sd)**2
    pi = 3.1415926
    denom = (2*pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def getProb(x, rating, val):
    return normpdf(x, count[rating][val]["mean"],count[rating][val]["sd"])
def getProbRat(scores, rating):
    tot=TOT[rating]/TOT["sum"]
    for i in [-2,-1,0,1,2]:
        tot=tot*getProb(scores[i], rating, i)
    return tot
def mostLikely(scores):
    max,val=0,-1
    for i in [0,1,2,3,4,5,6,7,8,9,10]:
        curr=getProbRat(scores, i)
        if curr>max:
            max=curr
            val=i
    return val

#---------------------TEST------------------------#
data=train(ratings, sentiments)
count=stat(data)
scores={-2:0,-1:0,0:1,1:2,2:3}
#populate testing data
test={}
for RID, sents in sentiments.iteritems():
    test[RID]={-2:0,-1:0,0:0,1:0,2:0}
    for k in sents:
        val=k[1]
        test[RID][val]=data[RID][val]+1


#run testing data
dist=[0,0,0,0,0,0,0,0,0,0,0]
for  RID, vals in test.iteritems():
    pred=mostLikely(vals)
    actual=int(ratings[RID])
    err=int(math.fabs(actual-pred))
    dist[err]=dist[err]+1

s=sum(dist)
i=0
st=[0,0,0,0,0,0,0,0,0,0,0]
while i<11:
    st[i]=dist[i]/s
    i=i+1

print st
