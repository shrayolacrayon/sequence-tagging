def findIndex(slist, observationList, fileName, backTrack):
	observationNumber= 0
	sentenceNumber= 0
	output= open(fileName, "w")
	backTrack.reverse()
	print "This is the number of sentences: "+str(len(slist))
	print "This is the number of observations: "+str(len(observationList))
	print "BACKTRACK"
	print backTrack
	print "The length of backtrack is : "+str(len(backTrack))
	for t in range(0,len(slist)):
		for o in range(0,len(observationList)):
			print "OBBBBBBBBBBBSSSSSSSSSSSS"
			print observationList[o]
			if t in observationList[o]:
				observationNumber= o
				print "I GOTTTTT INNNNN"
				#print "NUMBERRRRRR: "+str(observationNumber)
				#sentenceNumber= observationList[o].index(t)
				sentiment= backTrack[observationNumber]
				if t == 0:
					#print "this is the first sentiment: "+str(sentiment)
					output.write(str(sentiment))
				else:
					output.write("\n"+str(sentiment))
	output.close()
				




