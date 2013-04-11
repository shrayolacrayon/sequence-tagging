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
  sent,state = sentence
  words = sent.split()
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
  freq_sent = sort_sentence(sentence)
  index = 0
  while index < len(freq_sent):
    for i, listed in enumerate(chunked_features):
      string, _ = freq_sent[index]
      if string in listed:
        full_list[i] = full_list[i] + [sentence_index]
        return
    index += 1
  add_to_end(full_list, sentence, c)


def place_all_sentences(slist, polar, capacity):
  chunked_features = group_features(polar['pos'], capacity)
  chunked_features += group_features(polar['neg'], capacity)
  chunked_features += group_features(polar['neut'], capacity)

  full_list = [[]] * len(chunked_features)
  for i,s in enumerate(slist):
    place_sentence(s,full_list,i,chunked_features, capacity)
  return full_list

def add_sentence(s,observation, n):
  observation[n] = observation[n] + [s]

#observations: [one pos, one neg, one neutral, onepos-oneneg,more than one pos, more than one neg, more than one neutral, unknown]
def place_by_features(polar, sentence, observation,index,s, obs_ind):
  pos = 0
  neg = 0
  neutral = 0
  for p in polar['pos']:
    if p in sentence:
      pos += 1
  for n in polar['neg']:
    if n in sentence:
      neg += 1
  for n in polar['neut']:
    if n in sentence:
      neutral += 1
  tupled = (pos,neg,neutral)

  if pos == 1 and neg == 1:
    #one positive
    add_sentence(s, observation,3 )
    add_sentence(index, obs_ind,3 )
  elif neg == 1 and pos == 0:
    add_sentence(s, observation,1)
    add_sentence(index, obs_ind,1 )
  elif pos == 1:
    add_sentence(s,observation, 0)
    add_sentence(index, obs_ind,0 )
  elif tupled == (0,0,1):
    add_sentence(s,observation, 2)
    add_sentence(index, obs_ind,2 )
  elif pos > 1:
    add_sentence(s, observation, 4)
    add_sentence(index, obs_ind,4 )
  elif neg > 1:
    add_sentence(s,observation,5)
    add_sentence(index, obs_ind,5 )
  elif neutral > 1: 
    add_sentence(s, observation, 6)
    add_sentence(index, obs_ind,6 )
  else:
    add_sentence(s, observation, 7)
    add_sentence(index, obs_ind,7)

def place_all_features(slist, polar):
  observation = [[]] * 8
  obs_ind = [[]] * 8
  for i,s in enumerate(slist):
    sentence, state = s
    place_by_features(polar,sentence,observation,i,s, obs_ind)
  return observation, obs_ind


  














