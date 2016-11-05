from random import choice
from sys import argv


'''
input housekeeping 
shoots to remove as many 'non-dupes' as possible:

" StrIng\" == "string" == "string\n"

so we can correlate more parts of a diverse text 

'''
def cleanString( _string ):
	string = _string.strip()

	for badchar in ["/","\\","\n","\t","\r"]:
		string = string.replace(badchar, "")

	return string.lower()

def stripSpaces( _string ):
	return _string.replace(" ", "")

def cleanList( _list ):
	sanitized = []
	for word in _list:
		word = stripSpaces(word)
		if word not in ["", ".", "?", "!"]:
			sanitized.append(word)
	return sanitized

'''
markov stuff

'''
def mDictFromString( _string ):
	'''
	the structure: for each word in corpus, sanitize and add
	to dict as key WORD. then iterate across corpus by dict keys
	and add word N+1 to key WORD's array. 

	since duplicate values are added to arrays, statistical probability
	is built in.

	dict['hello'] = ['world', 'world', 'mom']
	'''
	string = cleanString(_string)
	splitByWord = string.split(" ")
	sanitized = cleanList(splitByWord)
	mDict = {}

	for word in sanitized:
		mDict[word] = []

	for x in range(0, len(sanitized) - 1):
		key = sanitized[x]
		nextWord = sanitized[x+1] 
		mDict[key].append( nextWord )
	return mDict

def generateStringFromMDict( _mDict, wordCount=15, startWord=None ):
	'''
	the algorithm: take word, either preselected or at random,
	and find next candidate word by selecting from array at random.
	print first word, then repeat process to candidate word until
	the word counter runs up.
	'''
	previousWord = ""
	currentWord = ""
	retString = ""

	if startWord == None:
		previousWord = choice( _mDict.keys() )
	else:
		previousWord = startWord

	retString = previousWord + " "

	try:
		for x in range(0, wordCount):
			currentWord = choice( _mDict[previousWord] )
			retString += currentWord + " "
			previousWord = currentWord

	except KeyError:
		pass

	return retString


'''

make some magic

'''
if __name__ == "__main__":

	if not len(argv) > 1:
		print "Please provide a filename to source corpus"
		print "  python markovify.py source.txt"
		print ""
		print "Optional: pass a seed word"
		print "  python markovify.py source.txt SEED"
		exit(1)

	missedDict = {}

	with open(
		"./missedconnections.txt"
	) as file:
		missedDict = mDictFromString( file.read() )

	if len(argv) > 2:
		print ( generateStringFromMDict(
			missedDict,
			wordCount = 400,
			startWord = argv[2]
		))

	else:
		print ( generateStringFromMDict(
			missedDict,
			wordCount = 400
		))
