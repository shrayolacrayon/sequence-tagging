import train
import random
#choose ngrams that are the most popular and that cover all of the sentences.
#sort the ngrams by the size of the array
#keep going until you get to having all of the sentences (counter)

#makes a list of tuples with the ngram and the number of sentences in that list
def dict_to_tuple(ngram_dict):
  full_list = []
  for key in ngram_dict:
    full_list.append((len(ngram_dict[key]), key))
  full_list=  sorted(full_list)
  full_list.reverse()
  return full_list

#adds to the end unless capacity of the last is full
def add_to_end(full_list, s_ind,capacity):
  if len(full_list[-1]) >= capacity:
    full_list.append([s_ind])
  else:
    full_list[-1].append(s_ind)

def condense_singles(obs_index, observations):
  unknown_ind = 0
  for i, o in enumerate(observations):
    if len(o) <= 1:
      unknown_ind = i
      break;
  new_obs = observations[:unknown_ind]
  new_ind = obs_index[:unknown_ind]
  for i in range(unknown_ind, len(observations)):
    add_to_end(new_obs, observations[i][0], 5)
    add_to_end(new_ind, obs_index[i][0], 5)
  return new_obs, new_ind, unknown_ind

#ngram method- group the sentences by ones with the most similar ngrams
def max_each_sent(ngram_dict, slist):
  observations = []
  obs_index = []
  ngrams= []
  sorted_list = dict_to_tuple(ngram_dict)
  #added into an observation
  added = [0] * len(slist)
  list_index = 0
  while 0 in added and list_index < len(sorted_list):
    amt, ngram = sorted_list[list_index]
    sent_list = ngram_dict[ngram] 
    o_n = []
    o_i = []
    for s in sent_list:
      if added[s] == 0:
        added[s] += 1
        a =slist[s]
        o_i.append(s)
        o_n.append(a)
    if o_n != []:
      ngrams.append(ngram)
      observations.append(o_n)
      obs_index.append(o_i)
    list_index += 1
  new_obs, new_ind, unknown_ind = condense_singles(obs_index, observations)
  return obs, obs_index, ngrams[:unknown_ind], unknown_ind


#ngrams is the list of definite ngrams 
def group_by_ngrams(ngram_dict, slist, ngrams, unknown_ind, bound):
  mapped = [[]] * bound
  sorted_list = dict_to_tuple(ngram_dict)
  added = [0] * len(slist)
  list_index = 0
  for amt, ngram in sorted_list:
    if ngram in ngrams:
      index = ngrams.index(ngram)
      sent_list = ngram_dict[ngram]
      for s in sent_list:
        if added[s] == 0:
          m = mapped[index]
          newl = m + [s]
          mapped[index] = newl
          added[s] += 1
  for i,a in enumerate(added):
    if a == 0:
      a += 1
      r = random.randint(unknown_ind, len(ngrams))
      mapped[r].append(i)
  return mapped


#returns a list of list of observations
def sent_to_obs(ngram_dict, slist, function):
  if function == "ngram":
    return max_each_sent(ngram_dict,slist)
  else:
    return [],[]
  



