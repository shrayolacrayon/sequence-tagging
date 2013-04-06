import nltk

#aMatrix and bMatrix are dicts, ngramSentence and stateList are lists
def virterbiTotal(aMatrix, bMatrix, observationList):
	vertMatrix= {}
	backPointer= {}
	for x in range(0,5):
		vertMatrix[stateConverter(x)]=[]
		vertMatrix[stateConverter(x)].append(1 * bMatrix[0][x])
		backPointer[stateConverter(x)]= []
		backPointer[stateConverter(x)].append(0)
	for t in range(1,len(observationList)):
		for s in range(0,5):
			(mState, mNum)= virterbiMax(vertMatrix,(t-1), aMatrix, s)
			vertMatrix[stateConverter(s)].append(mNum * bMatrix[observationList[t][s]])
			backPointer[stateConverter(s)].append(mState)

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


def virterbiMax(vertMatrix, counter, aMatrix, s):
	maxNum= 0.0
	maxState= 3.0
	for vert in vertMatrix:
		varying= vertMatrix[vert][counter] * aMatrix[s][stateConverterOpp(vert)]
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

def stateConverter(number):
	stateI=0;
	if number == 0:
		stateI= -2
	elif number == 1:
		stateI= -1
	elif number == 2:
		stateI= 0
	elif number == 3:
		stateI= 1
	else:
		stateI= 2
	return stateI

def stateConverterOpp(state):
	nums=0;
	if state == -2:
		nums= 0
	elif state == -1:
		nums= 1
	elif state == 0:
		nums= 2
	elif state == 1:
		nums= 3
	else:
		nums= 4
	return nums

def create_gram_list(sentiments, gramType):
  gram_list = []
  for key in sentiments:
    sent_list = sentiments[key]
    for (string, sent) in sent_list:
      tokens = nltk.word_tokenize(string)
      grams = nltk.util.ngrams(tokens,gramType)
      gram_list.append(grams)
  return gram_list