#hmm.py

import nltk

import parse
import train


import os
path = 'train/'

listing = os.listdir(path)
#iterate through listing
for fname in listing:
  ratings,sents=  parse.parse(path + fname)
  print "RATINGS"
  print ratings
  print "SENTS"
  #print sents
  print train.create_probabilities(sents, 1)

