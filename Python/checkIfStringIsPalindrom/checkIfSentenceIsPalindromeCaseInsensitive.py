def checkIfSentenceIsPalinrome(sentence):
	newSen = sentence.lower()
	print newSen

	start = 0
	end = len(newSen)-1

	mid = (start + end)/2

	while start < end:
		while newSen[start].isalnum() is False and start < end:
			start = start + 1
		while newSen[end].isalnum() is False and start < end:
			end = end - 1

		if newSen[start] != newSen[end]:
			print "Sentence not a palindrome"
			return

		start = start + 1
		end = end - 1

	print "Sentence is a palindrome"

def main():
	sentence = "A man, a plan, a canal: Panama."
	checkIfSentenceIsPalinrome(sentence)
	sentence = ".........."
	checkIfSentenceIsPalinrome(sentence)
	sentence = 'a'
	checkIfSentenceIsPalinrome(sentence)
	sentence = "1 2 3 4 5 6 5 4 3 2 1 "
	checkIfSentenceIsPalinrome(sentence)

if __name__ == '__main__':
	main()