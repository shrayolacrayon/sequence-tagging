import nltk
import parse

(ratings, sentiments, sent_list)= parse.parse('train/ScottRenshaw_train.txt')

print sentiments

#returns a list of list of observations
#def sent_to_obs(sentiments):
  
