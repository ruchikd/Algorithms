class Word:
	def __init__(self, data, index):
		self.data = data
		self.index = index

def printAnagrams(arr):
	dupArray = []
	size = len(arr)

	for i in range(size):
		dupArray.append(Word(arr[i], i))

	for i in range(size):
		dupArray[i].data = ''.join(sorted(dupArray[i].data))

	dupArray = sorted(dupArray, key=lambda x: x.data)

	for i in range(size):
		print arr[dupArray[i].index]

def main():
	print "Hello, world"
	arr = ["dog", "act", "cat", "god", "tac"]

	printAnagrams(arr)

if __name__== '__main__':
	main()