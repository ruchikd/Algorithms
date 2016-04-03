def maxProduct(words):
	if len(words) == 0:
		return 0

	if len(words) == 1:
		return len(words)

	d1 = dict()
	word = words[0]
	for w in word:
		d1[w] = True
	word1 = words[0]
	print d1

	word1, word2 = None, None
	for word in words:
		print word
		newWord = True
		for w in word:
			print w
			if w in d1.keys():
				newWord = False
				break

def main():
	words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
	print words

	print maxProduct(words)

if __name__ == '__main__':
	main()