import nltk

def createBMatrix(ngrams, ngramProbs):
	matrix= {}
	for ngram in ngrams:
		if ngram in ngramProbs:
			matrix[ngram]=ngramProbs[ngram]
		else:
			matrix[ngram]=[0.1,0.1,0.1,0.1,0.1]
	return matrix

#aMatrix and bMatrix are dicts, ngramSentence and stateList are lists
def virterbiTotal(aMatrix, bMatrix, ngramSentence, stateList):
	vertMatrix= {}
	backPointer= {}
	for x in range(0,len(stateList)):
		vertMatrix[stateList[x]]=[]
		vertMatrix[stateList[x]].append(aMatrix[stateList[x]][0] * bMatrix[ngramSentence[0]][stateConverter(stateList[x])])
		backPointer[stateList[x]]= []
		backPointer[stateList[x]].append(0)
	for t in range(1,len(ngramSentence)):
		for s in range(0,len(stateList)):
			(mState, mNum)= virterbiMax(vertMatrix,(t-1), aMatrix, stateList, s)
			vertMatrix[stateList[s]].append(mNum * bMatrix[ngramSentence[t]][stateConverter[s]])
			backPointer[stateList[s]][t].append(mState)

	(finState, finNum)= finalVert(vertMatrix,-1,aMatrix,stateList)

	vertMatrix["final"]= finNum
	backPointer["final"]= finState
	return createBackTrack(backPointer)


def createBackTrack(backPointer):
	back=[backPointer["final"]]
	last= backPointer["final"]
	for t in range(2,len(ngramSentence)):
		current= backPointer[last][len(ngramSentence)-t]
		back.append(current)
		last= current
	return back


def virterbiMax(vertMatrix, counter, aMatrix, stateList, s):
	maxNum= 0.0
	maxState= 3.0
	for vert in vertMatrix:
		varying= vertMatrix[vert][counter] * aMatrix[stateList[s]][stateConverter(vert)]
		if varying >= maxNum:
			maxNum= varying
			maxState= vert
	return maxState, maxNum	

def finalVert(vertMatrix, counter, aMatrix, stateList):
	fiNum= 0.0
	fiState= 3.0
	for vert in vertMatrix:
		fin= vertMatrix[vert][counter] * aMatrix["final"][stateConverter(vert)]
		if fin >= fiNum:
			fiNum= fin
			fiState= vert
	return fiState, fiNum

def stateConverter(state):
	count=0;
	if state == -2:
		count= 1
	elif state == -1:
		count= 2
	elif state == 0:
		count= 3
	elif state == 1:
		count= 4
	else:
		count= 5

def create_gram_list(sentiments, gramType):
  gram_list = []
  for key in sentiments:
    sent_list = sentiments[key]
    for (string, sent) in sent_list:
      tokens = nltk.word_tokenize(string)
      grams = nltk.util.ngrams(tokens,gramType)
      gram_list.append(grams)
  return gram_list