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
  for i,m in enumerate(matrix):
    normalized[i] = float(m)/len(matrix)
  return normalized

#counts the number of sentiments
def count_sentiments(sentiments):
  #create a 1 * 5 matrix of s_count
  s_count = [0] * 5
  for key in sentiments:
    sent_list = sentiments[key]
    for (string, sent) in sent_list:
      s_count[sent_to_index(sent)] += 1
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







