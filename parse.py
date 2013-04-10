
def parse_rating(string):
  splitted = string.split('/');
  return (splitted[0], splitted[1].strip('] '))

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def parse (filename):
  #dictionary ratings has the key, review_id with the rating given
  #note ratings are different for different authors
  ratings = {}
  #key = review-id, value is a list of tuples with sentiment 
  #and the actual phrase
  sentiments= {}

  sent_list = []
 
 
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
        if is_int(second):
          s = int(second)
        else:
          s = second
        sentiments[rid].append((first,s))
        sent_list.append((first,s))
       

  return(ratings, sentiments, sent_list)



