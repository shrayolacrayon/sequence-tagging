def findIndex(slist, observationList, fileName, backTrack):
	observationNumber= 0
	sentenceNumber= 0
	output= open(fileName, "w")
	backTrack.reverse()
	#print "This is the number of sentences: "+str(len(slist))
	#print "This is the number of observations: "+str(len(observationList))
	#print "BACKTRACK"
	#print backTrack
	#print "The length of backtrack is : "+str(len(backTrack))
	for t in range(0,len(slist)):
		for o in range(0,len(observationList)):
			if t in observationList[o]:
				observationNumber= o
				sentiment= backTrack[observationNumber]
				if t == 0:
					output.write(str(sentiment))
				else:
					output.write("\n"+str(sentiment))
				
	output.close()
				
def findIndexSVM(slist, observationList, fileName, backTrack):
	observationNumber= 0
	sentenceNumber= 0
	output= open(fileName, "w")
	backTrack.reverse()
	#print "This is the number of sentences: "+str(len(slist))
	#print "This is the number of observations: "+str(len(observationList))
	#print "BACKTRACK"
	#print backTrack
	#print "The length of backtrack is : "+str(len(backTrack))
	for t in range(0,len(slist)):
		for o in range(0,len(observationList)):
			if t in observationList[o]:
				observationNumber= o
				sentiment= backTrack[observationNumber]
				if t == 0:
					output.write(str(sentiment))
				else:
					output.write("\n"+str(sentiment))
				t= -50
	output.close()




