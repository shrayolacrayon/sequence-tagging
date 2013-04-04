#create matrix in the form of a dictionary
import nltk

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

def normalize_p(sents):
  normalized = []
  slen = float(len(sents))
  for x in range(-2,2):
    normalized.append(sents.count(x)/slen)
  return normalized

#count the number of each and normalize
def create_probabilities(sentiments, gramType):
  mapped = map_grams(sentiments,gramType)
  matrix = {}
  for m in mapped:
    matrix[m] = normalize_p(mapped[m])
  return matrix


