def findIndex(obs_sent_Indexes, slist, observationList, fileName, backTrack):
	observationNumber= 0
	sentenceNumber= 0
	output= open(fileName, "w")
	print "This is the number of sentences: "+str(len(slist))
	print "This is the number of observations: "+str(len(observationList))
	for t in range(0,len(slist)):
		for o in range(0,len(obs_sent_Indexes)):
			if t in obs_sent_Indexes[o]:
				observationNumber= o
				sentenceNumber= obs_sent_Indexes[o].index(t)
				sentiment= backTrack[-o]
				if t == 0:
					print "this is the first sentiment: "+str(sentiment)
					output.write(str(sentiment))
				else:
					output.write("\n"+str(sentiment))
				




