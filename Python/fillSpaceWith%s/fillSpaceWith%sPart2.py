def fillSpace(sentence):
	if sentence is None:
		return None

	newSentence = []
	for character in sentence:
		if character == ' ':
			newSentence.append('%')
			newSentence.append('0')
			newSentence.append('2')
		else:
			newSentence.append(character)

	print ''.join(newSentence)

def main():
	str = "Hi my name is Ruchik Samir Dave"
	str = None
	str = "s"
	str = ' '

	fillSpace(str)

if __name__ == '__main__':
	main()