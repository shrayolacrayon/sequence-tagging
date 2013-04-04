#hmm.py

import nltk
import parse
import train

ratings,sents=  parse.parse('train/ScottRenshaw_train.txt')
print "RATINGS"
print ratings
print "SENTS"
#print sents
print train.create_probabilities(sents, 0)