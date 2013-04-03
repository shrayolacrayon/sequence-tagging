def parse_rating(string):
  splitted = string.split('/');
  return (splitted[0], splitted[1].strip('] '))

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
      line_stripped = line.strip()
      lsplit = line_stripped.split('<')
      if len(lsplit) == 1:
        pass
      else:
        first = lsplit[0].strip("{} ")
        second = lsplit[1].strip("> ")
        sentiments[rid].append((first,int(second)))

  return(ratings, sentiments)



