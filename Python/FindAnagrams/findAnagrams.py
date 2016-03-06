class Word(object):
	def __init__(self, word, index):
		self.word = word
		self.index = index

def createDupArray(arr):
	dupArray = []

	for i in range(len(arr)):
		dupArray.append(Word(arr[i], i))

	return dupArray

def main():
	arr = ["cat", "dog", "act", "god", "dgo", "tca"]

	dupArray = createDupArray(arr)
	for i in range(len(dupArray)):
		dupArray[i].word = ''.join(sorted(dupArray[i].word))

	for i in range(len(dupArray)):
		dupArray = sorted(dupArray, key=lambda k : k.word)

	for i in range(len(dupArray)):
		print arr[dupArray[i].index]

if __name__ == '__main__':
	main()