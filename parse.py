def parse_rating(string):
  splitted = string.split('/');
  return (splitted[0], splitted[0])

def parse (filename):
  #dictionary ratings has the key, review_id with the rating given
  #note ratings are different for different authors
  ratings = {}
  #key = review-id, value is a list of tuples with sentiment 
  #and the actual phrase
  sentiments= {}
  rid = "null"
  files = open(filename)
  for line in files:
    #new rid to look at
    if line[0] == '[':
      (rid,rating) = parse_rating(line[1:-1])
      ratings[rid] = rating
      sentiments[rid] = []
    else:
      sentiments[rid] = line.strip("{} ")



