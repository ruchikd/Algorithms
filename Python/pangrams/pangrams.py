def checkIfPangrams(sentence):
	sentence = sentence.lower()
	alphabetList = [False]*26

	for x in range(len(sentence)):
		if sentence[x].isalpha() == False:
			continue
		alphabetList[ord(sentence[x]) - 97] = True

	if False in alphabetList:
		print "\"", sentence, "\" is not a pangram"
	else:
		print "\"", sentence, "\" is a pangram"

checkIfPangrams("Pack my box with five dozen liquor jugs.")
checkIfPangrams("The quick brown fox jumps over the lazy dog.")