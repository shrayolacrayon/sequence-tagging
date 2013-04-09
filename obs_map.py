
import train

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

#ngram method- group the sentences by ones with the most similar ngrams
def max_each_sent(ngram_dict, slist):
  observations = []
  sorted_list = dict_to_tuple(ngram_dict)
  #added into an observation
  added = [0] * len(slist)
  list_index = 0
  while 0 in added and list_index < len(sorted_list):
    amt, ngram = sorted_list[list_index]
    sent_list = ngram_dict[ngram] 
    o_n = []
    for s in sent_list:
      if added[s] == 0:
        added[s] += 1
        a =slist[s]
        o_n.append(a)
    if o_n != []:
      observations.append(o_n)
    list_index += 1
  return observations



#returns a list of list of observations
def sent_to_obs(ngram_dict, slist, function):
  if function == "ngram":
    return max_each_sent(ngram_dict,slist)
  else:
    return []
  



