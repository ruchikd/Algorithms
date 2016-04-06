def checkIfStrHasUniqueChars(word):
	d = dict()
	unique = True

	if word == None:
		print "The given string is None"
		return

	for w in word:
		if w not in d.keys():
			d[w] = True
		else:
			unique = False
			break

	if unique == True:
		print "The given string", word, "has all unique characters"
	else:
		print "The given string", word, "doesnt have all unique characters"


def main():
	#str = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
	str = 'a'
	checkIfStrHasUniqueChars(str)

if __name__ == '__main__':
	main()