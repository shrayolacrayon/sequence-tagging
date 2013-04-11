#hmm.py

import nltk
import os

import parse
import train
import test
import obs_map
import file_Maker

path = 'train/'
testpath = 'test/'
testing = 'test_train/'
listing = os.listdir(path)
testlisting = os.listdir(testpath)
#iterate through listing
for fname in listing:
  ratings,sents, slist=  parse.parse(path + fname)
  #print sents
  if fname == "DennisSchwartz_train.txt":
    ratingsTest, sentsTest, slistTest= parse.parse(testpath + "DennisSchwartz_test.txt")
  else:
    ratingsTest, sentsTest, slistTest= parse.parse(testpath + "ScottRenshaw_test.txt")
  print "Length of slist at the top: "+str(len(slist))
  print "RATINGS"
  print "SENTS"
  print "P(sent)"
  count_s =  train.count_sentiments(sents)
  #print count_s
  print "S i|j"
  aMatrix= train.sentiment_i_j(slist, count_s)
  #print aMatrix
  print "creating ngram..."
  ngram_dict= train.ngrams_index(slist,2)
  
  print "OBSERVATIONS"
  observations, obs_indexes, nGramUnknown, unknownIndex= obs_map.max_each_sent(ngram_dict,slist)
  #print observations
  #print obs_indexes
  print "OBS PROBS"
  b_matrix= train.observation_state(observations, slist,count_s)
  print "Initial Probabilities"
  initProbs= train.initialProb(sents)
  print "finding the test sentences via observations..."
  testGrouped= obs_map.group_by_ngrams(ngram_dict, slist, nGramUnknown, unknownIndex, len(observations))
  #print initProbs
  print "trying to find the sents"
  back_trace= test.virterbiTotal(aMatrix, b_matrix, testGrouped,initProbs)
  print back_trace
  print "creating results textFile"
  file_Maker.findIndex(slistTest,testGrouped,testing+fname,back_trace)


  #print train.observation_state(observations,slist,count_s)
  