import obs_map
import os

from collections import Counter

path = 'features/'
#takes in a file and returns a list of features
def parse_features(fname):
  features = []
  feature_file = open(fname)
  for line in feature_file:
    splitted = line.split(',')
    features.append(splitted[0].lower())  
  return features


def features():
  positive = parse_features(path+ 'positive.csv')
  negative = parse_features(path + 'negative.csv')
  return positive, negative


def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

#make arbitrary groupings of words
def group_features(feature_list, n):
  list_length = len(feature_list)
  if n >= list_length:
    return feature_list
  amt_wanted = list_length/n
  chunked_features = chunks(feature_list,amt_wanted)
  return chunked_features

#adds to the end unless capacity of the last is full
def add_to_end(full_list, s_ind,capacity):
  if len(full_list[-1]) >= capacity:
    full_list.append([s_ind])
  else:
    full_list[-1].append(s_ind)


#returns a dictionary of the frequencies
def sort_sentence(sentence):
  s_dict= {}
  words = sentence.split()
  for w in words:
    if w not in s_dict:
      s_dict[w] = 1
    else:
      s_dict[w]+= 1
  tupled = list(s_dict.items())
  tupled= sorted(tupled)
  tupled.reverse()
  return tupled
  
#figure out the frequency of each word
#if its not in the features list, then add it to an arbitrary list
#the arbitrary list can only have a max of 5 sentences in it
def place_sentence(sentence, full_list, sentence_index, chunked_features, c):
  freq_sent = sort_sentence(sentece)
  index = 0
  while index < len(freq_sent):
    for i, listed in enumerate(chunked_features)
      string, _ = freq_sent[index]
      if string in listed:
        full_list[i] = full_list[i] + [sentence_index]
        return
    index += 1
  add_to_end(full_list, sentence, c)

def place_all_sentences(slist):
  full_list = []
  for s in slist:







