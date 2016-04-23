def palindromePairs(words):
	if words is None:
		return None

	bigList = []
	for word in words:
		for w in words:
			if w == word:
				continue
			posPalindrome = w + word
			if posPalindrome == posPalindrome[::-1]:
				smallList = []
				smallList.append(words.index(w))
				smallList.append(words.index(word))
				if smallList not in bigList:
					bigList.append(smallList)
			posPalindrome = word + w
			if posPalindrome == posPalindrome[::-1]:
				smallList = []
				smallList.append(words.index(word))
				smallList.append(words.index(w))
				if smallList not in bigList:
					bigList.append(smallList)

	return bigList

def main():
	words = ["abcd","dcba","lls","s","sssll"]

	print palindromePairs(words)

if __name__ == '__main__':
	main()