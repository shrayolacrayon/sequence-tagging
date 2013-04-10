#hmm.py

import nltk
import os

import parse
import train
import test
import obs_map

path = 'train/'
testpath = 'test/'
testing = 'test_train/'
listing = os.listdir(path)
testlisting = os.listdir(testpath)
#iterate through listing
for fname in listing:
  ratings,sents, slist=  parse.parse(path + fname)
  print "RATINGS"
  #print ratings
  print "SENTS"
  #print slist
  print "P(sent)"
  count_s =  train.count_sentiments(sents)
  print count_s
  print "S i|j"
  print train.sentiment_i_j(slist, count_s)
  print "creating ngram..."
  ngram_dict= train.ngrams_index(slist,3)
  print "OBSERVATIONS"
  observations= obs_map.max_each_sent(ngram_dict,slist)
  print observations
  print "OBS PROBS"
  #print train.observation_state(observations,slist,count_s)
  