'''

TO DO

treat punctuation as 'a word' ::
	["string...", "xx"] -> ["string", "...", "xx"]
	(still strip newlines tho??)
'''

from random import choice
from sys import argv


'''
input housekeeping 
shoots to remove as many 'non-dupes' as possible:

" StrIng\" == "string" == "string\n"

so we can correlate more parts of a diverse text.

some punctuation is OK, because it helps retain the 
aesthetic sense of the source text. 

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
	and add word N+1 to key WORD's NEXT array. Same goes for PREV
	but in reverse.

	mDict {
		WORD {
			PREV: [],
			NEXT: [],
			SYLLABLES: int
		},
		WORD2 {},
		...
	}


	since duplicate values are added to arrays, statistical probability
	is built in.

	dict['hello']['next'] = ['world', 'world', 'mom']
	dict['hello']['prev'] = ['say', 'well', 'hello']
	'''
	string = cleanString(_string)
	splitByWord = string.split(" ")
	sanitized = cleanList(splitByWord)
	mDict = {}

	for word in sanitized:
		mDict[word] = {}
		mDict[word]['next'] = []
		mDict[word]['prev'] = []
		mDict[word]['syllables'] = countSyllables(word)

	mDictRange = len(sanitized) - 1

	# words that follow
	for x in range(0, mDictRange):
		key = sanitized[x]
		nextWord = sanitized[x+1] 
		mDict[key]['next'].append( nextWord )

	# words that precurse
	for x in range(0, mDictRange):
		key = sanitized[x]
		if x > 0:
			prevWord = sanitized[x-1]
			mDict[key]['prev'].append( prevWord )

	return mDict

def generateTextForward( _mDict, wordCount=15, startWord=None ):
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
			currentWord = choice( _mDict[previousWord]['next'] )
			retString += currentWord + " "
			previousWord = currentWord

	except KeyError:
		pass

	return retString


def generateTextBackward( _mDict, wordCount=15, startWord=None):
	'''

	Same as before, but working in reverse. 

	'''

	previousWord = ""
	currentWord = ""
	retString = ""

	if startWord == None:
		previousWord = choice( _mDict.keys() )
	else:
		previousWord = startWord

	retString = ""

	try:
		for x in range(0, wordCount):
			currentWord = choice( _mDict[previousWord]['prev'] )
			retString = previousWord + " " + retString
			previousWord = currentWord

	except KeyError:
		pass

	return retString

def generateTextFromMiddle( _mDict, wordCountForward=15, wordCountBackward=15, startPhrase="hello world"):
	'''

	A little trickery to put choice phrases of our design 
	here and there, ro regain a little authorial control 

	'''
	startPhraseList = startPhrase.split(" ")

	# generate preamble
	retString = generateTextBackward( _mDict, wordCountBackward, startPhraseList[0])

	# insert remainder of phrase (if greater than two words)
	if len(startPhraseList) > 2:
		for word in startPhraseList[1:-1]:
			retString += word + " "

	# generate remainder of text
	retString += generateTextForward( _mDict, wordCountForward, startPhraseList[-1])

	return retString

def generateTextBySyllablePattern( _mDict, pattern, startWord=None ):
	'''

	pattern is a string representing syllable count
	per line, e.g.,: "5 7 5" will output a haiku

	'''
	prevWord = None
	currentWord = None
	retString = ""

	patternList = pattern.split(" ")
	triesPerLine = 10000

	if startWord == None:
		prevWord = choice(_mDict.keys())
	else:
		prevWord = startWord 

	for syllableMax in patternList:
		lineTries = 0
		#computer gets 10000 tries to get syllables right
		countedWords = []
		while lineTries < triesPerLine:
			currentWord = choice( _mDict[prevWord]['next'])
			countedWords.append(currentWord)
			prevWord = currentWord

			#check syllable count
			count = 0
			for word in countedWords:
				count += _mDict[word]['syllables']
			
			if count > int(syllableMax):
				#over. bust. try again.
				countedWords = []

			elif count == int(syllableMax):
				#even. break free.
				retString += ' '.join(countedWords) + "\n"
				break

	return retString


def countSyllables(word):
	'''
	naive syllable counting for english, mostly correct,
	adapted from http://codegolf.stackexchange.com/a/47325
	'''

	count = 0

	nonevowels = ['a','i','o','u','y']
	badendings = ['d','ly']
	wordlen = len(word) - 1

	for charindex in range(0, wordlen):
		if charindex < wordlen:
			
			#vowel runs
			if word[charindex] in nonevowels:
				if word[charindex+1] in nonevowels:
					count += 1

			#good Es 
			if word[charindex] is "e":
				if word[charindex+1:-1] not in badendings:
					count += 1

			#trailing LE 
			if word[-2:-1] is "le":
				count += 1

		if word[charindex] in nonevowels:
			#otherwise, vowels interrupt consonants
			count += 1

	return count

helptext = """

markovify.py

simple markov-chain text analysis and synthesis on the command 
line for art, poetry, fun and profit.

written by kevin bott, inspired by daniel shiffman 

-----

usage:

$ python markovify.py [filename] [options]

optional flags:

	--gentype, -g
		can be either FORWARD, BACKWARD, or MIDDLEOUT

		forward and backward have optional SEEDWORD flag

		middleout requires SEEDPHRASE flag

	--length, -l
		number of words to output

	--seedword, -sw
		begin or end output with specific word, depending 
		on GENTYPE 

	--seedphrase, -sp
		phrase to place in middle of output with MIDDLEOUT gentype

	--help, -h
		display this helpful wall of text

	--dump, -d
		dump data structure to terminal. experimental. mostly
		for debugging new features. 

examples:

	$ python markovify.py holy_bible.txt -l 5

	would generate 5 words likely to follow one another in the bible,
	whereas

	$ python markovify.py holy_bible.txt -g middleout \\
	-sp "hello world" -l 50

	would generate 50 words on either side of the phrase 
	"hello strange new world," with statistically likely words 
	preceding "hello" and following "world." 

	finally, 

	$ python markovify.py holy_bible.txt -g sylpattern \\
	-sp "5 7 5" 

	would try (10000 times per line) to generate a haiku

"""

'''

make some magic

'''
if __name__ == "__main__":
	argvDict = {
		'gentype': None,
		'sp': None,
		'sw': None,
		'length': 15,
		'help': False,
		'dump': False
	}

	if not len(argv) > 1:
		argvDict['help'] = True

	for index in range(0, len(argv)):

		indexLower = argv[index].lower()
		
		if indexLower in ['--gentype', '-g']:
			argvDict['gentype'] = argv[index + 1]
		
		if indexLower in ['--length', '-l']:
			argvDict['length'] = int(argv[index + 1])

		if indexLower in ['--seedword', '-sw']:
			argvDict['sw'] = argv[index + 1]

		if indexLower in ['--seedphrase', '-sp']:
			argvDict['sp'] = argv[index + 1]

		if indexLower in ['--help', '-h']:
			argvDict['help'] = True

		if indexLower in ['--dump', '-d']:
			argvDict['dump'] = True

	if argvDict['help'] == True:
		print helptext
		exit()

	missedDict = {}

	with open(
		argv[1]
	) as file:
		missedDict = mDictFromString( file.read() )


	if argvDict['dump'] == True:
		print missedDict
		exit()

	
	if argvDict['gentype'] in ["forward", None]:
		print( generateTextForward(
			missedDict,
			startWord = argvDict['sw'],
			wordCount = argvDict['length']
		))
	elif argvDict['gentype'] == "backward":
		print( generateTextBackward(
			missedDict,
			startWord = argvDict['sw'],
			wordCount = argvDict['length']
		))
	elif argvDict['gentype'] == "middleout":
		if argvDict['sp'] == None:
			print "Must provide seedphrase in quotes!"
			print "e.g., --seedphrase \"hello world\""
			exit()

		print( generateTextFromMiddle(
			missedDict,
			startPhrase = argvDict['sp'],
			wordCountForward = argvDict['length'],
			wordCountBackward = argvDict['length']
		))
	elif argvDict['gentype'] == "sylpattern":
		if argvDict['sp'] == None:
			print "Must provide syllable pattern in quotes!"
			print "e.g., --seedphrase \"5 7 5\" for a haiku"
			exit()

		print( generateTextBySyllablePattern(
			missedDict,
			pattern = argvDict['sp']
			))