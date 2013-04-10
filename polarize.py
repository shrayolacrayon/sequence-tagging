from __future__ import division
import nltk
from nltk.tokenize import word_tokenize
import parse
import operator
from nltk.corpus import wordnet as wn
(ratings, sentiments, sent_list)= parse.parse('train/ScottRenshaw_train.txt')

#get the num occurrances of a token t in that value
def get(t, val, uni):
        if t in uni[val]:
                return uni[val][t]
        else:
                return 1
        
#adds each token of a sentence to the unigram map
def add(sent, val, uni, count):
        count[val]=count[val]+1
        count["all"]=count["all"]+1
        for t in word_tokenize(sent):
                if t in uni[val]:
                        uni[val][t]=uni[val][t]+1
                else:
                        uni[val][t]=1
                if t in uni["all"]:
                        uni["all"][t]=uni["all"][t]+1
                else:
                        uni["all"][t]=1

#Create unigram distribution table
def train(sents):
        uni={-2:{},-1:{},-0:{},1:{},2:{},"all":{}}
        count={-2:0,-1:0,0:0,1:0,2:0,"all":0}
        for RID, sents in sentiments.iteritems():
                for s in sents:
                        curr_sent=s[0]
                        curr_val=s[1]
                        add(curr_sent, curr_val, uni, count)
        return uni, count

#find pos neg words
def wordTypes(uni, count):
        pos,neg,neut=[],[],[]
        for  tok in uni["all"].keys():
                vals={}
                verb=wn.synsets(tok, pos=wn.ADJ)
                adv=wn.synsets(tok, pos=wn.ADV)
                if len(verb)!=0 or len(adv)!=0:
                        for i in [-2,-1,0,1,2]:
                                vals[i]=get(tok, i, uni)
                        #determine if a word is pos, neg or neutral
                        if (vals[1]+vals[2]) > (vals[0]+vals[-1]+vals[-2])*1.25 :
                                pos.append(tok)
                        elif (vals[-1]+vals[-2]) > (vals[1]+vals[2]+vals[0])*1.5 :
                                neg.append(tok)
                        elif vals[0]>(vals[1]+vals[2]+vals[-1]+vals[-2])*1.5:
                                neut.append(tok)
        polars={"pos":pos, "neg":neg, "neut":neut}
        return polars

def countpolar(sent, polars):
        pos,neg,neut=0,0,0
        for t in word_tokenize(sent):
                if t in polars["pos"]:
                        pos=pos+1
                if t in polars["neg"]:
                        neg=neg+1
                if t in polars["neut"]:
                        neut=neut+1
        return [pos, neg, neut]

print "loading training data..."
u,c=train(sentiments)
print "DONE!"
print "getting word types..."
ps=wordTypes(u,c)
print "DONE!"
