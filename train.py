#create matrix in the form of a dictionary
import nltk

#transition, emission, observed/hidden variables 

#(ngram, sent)
def ngrams(tokens,n, sent, mapped):
  grams = nltk.util.ngrams(tokens,n)
  for g in grams:
    if g not in mapped:
      mapped[g] = [sent]
    else:
      mapped[g].append(sent)


#sentiments: ("rid": ("sentence",sentiment))
#prob_list (bigram: [sentiments...])
def map_grams(sentiments, gramType):
  mapped = {}
  for key in sentiments:
    sent_list = sentiments[key]
    for (string,sent) in sent_list:
      #tokenize it
      tokens = nltk.word_tokenize(string)
      if gramType == 0:
        ngrams(tokens,2,sent, mapped)
      elif gramType == 1:
        ngrams(tokens,3, sent, mapped)
  return mapped


#creates a dictionary of the number of each ngram in a sentece given a
#sentence, ngram type, and the index of the sentence in the list
def count_ngrams(sentence, n, index,ngram_dict):
  tokens = nltk.word_tokenize(sentence) 
  ngrams(tokens, n, index, ngram_dict)

def ngrams_index (slist,n):
  ngram_dict = {}
  for i,(s,sent) in enumerate(slist):
    count_ngrams(s,n, i, ngram_dict)
  return ngram_dict



#given a list sentiments, calculate the percentage of each sentiment
def normalize_p(sents):
  normalized = []
  slen = float(len(sents))
  for x in range(-2,3):
    normalized.append(sents.count(x)/slen)
  return normalized

#count the number of each and normalize
def create_probabilities(sentiments, gramType):
  mapped = map_grams(sentiments,gramType)
  matrix = {}
  for m in mapped:
    matrix[m] = normalize_p(mapped[m])
  return matrix

#converts to indexes needed
def sent_to_index(sentiment):
  return sentiment + 2
#normalizes matrix m
def normalize(matrix):
  normalized= [0.0] * len(matrix)
  summed = sum(matrix)
  for i,m in enumerate(matrix):
    if summed != 0:
      normalized[i] = float(m)/summed
    else:
      print "issue with" + str(matrix)
  return normalized

def count_sents(slist, s_count):
  for (string, sent) in slist:
      s_count[sent_to_index(sent)] += 1
  return s_count


#counts the number of sentiments and normalizes it
def count_sentiments(sentiments):
  #create a 1 * 5 matrix of s_count
  s_count = [0] * 5
  for key in sentiments:
    sent_list = sentiments[key]
    count_sents(sent_list, s_count)
  return normalize(s_count)


#creates a matrix of the previous sentiments given sentiment i
def calc_prev_matrix (i, slist, c):
  s_count = [0.0] * 5
  s_new = [0.0] * 5
  for x, (string, sent) in enumerate(slist):
    if sent == i:
      string, prev_sent= slist[x -1]
      s_count[sent_to_index(prev_sent)] += 1
  s_count = normalize(s_count)
  for j,s in enumerate(s_count):
    if c[j] != 0:

      s_new[j]= (s* c[sent_to_index(i)])/c[j]
  return s_new

#sentiments -> matrix of all with p[i][j] being the probabilty of 
#j given i. need: p(i) p(j) and p(j|i)
def sentiment_i_j(sent_list, count_s):
  s_matrix = []
  for i in range (-2, 3):
    s_matrix.append(calc_prev_matrix(i,sent_list,count_s))
  return s_matrix


def obs_states(observation):
  counter = [0] * 5
  for sentence, state in observation:
    counter[sent_to_index(state)] += 1
  return normalize(counter)

#p(o|s) = p(s|o) * p(o)/ p(s)
def one_observation(observation,count_s, slist):
  num_sents=  obs_states(observation)
  full = [0] * 5
  prob_o = float(len(observation))/len(slist)
  for i,n in enumerate(num_sents):
    full[i] = (n * prob_o)/count_s[i]
  return normalize(full)

def observation_state(observations, slist,count_s):
  matrx = []
  for o in observations:
    matrx.append(one_observation(o,count_s,slist))
  return matrx

def initialProb(sents):
  first_sentiments=[]
  for sentences in sents:
    first_sentiments.append(sents[sentences][0][1])
  #print first_sentiments
  initialProbs= [0] * 5
  for sentiment in first_sentiments:
    if sentiment == -2:
      initialProbs[0]= initialProbs[0] + 1
    elif sentiment == -1:
      initialProbs[1]= initialProbs[1]+1
    elif sentiment == 0:
      initialProbs[2] = initialProbs[2]+1
    elif sentiment == 1:
      initialProbs[3]= initialProbs[3] + 1
    else:
      initialProbs[4]= initialProbs[4]+1
  #print initialProbs
  
  for i in range(0,5):
    initialProbs[i]=initialProbs[i]/float(len(first_sentiments))
    
  print initialProbs
  #print initialProbs
  return initialProbs
















