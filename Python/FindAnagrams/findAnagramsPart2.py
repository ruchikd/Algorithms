def printAnagrams(words):
	wrapperList = []
	pos = 0

	for word in words:
		l = []
		l.append(word)
		l.append(pos)
		wrapperList.append(l)
		pos = pos + 1

	for l in wrapperList:
		l[0] = ''.join(sorted(l[0]))

	newList = sorted(wrapperList)

	anagramList = []
	for l in newList:
		print words[l[1]]
		anagramList.append(words[l[1]])

	return anagramList

def main():
	words = ['cat', 'het', 'act', 'some', 'the', 'mose', 'tac']
	print printAnagrams(words)

if __name__ == '__main__':
	main()