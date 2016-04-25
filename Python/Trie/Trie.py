class TrieNode:
	def __init__ (self, char):
		self.char = char
		self.children = []

def searchInTrie(trieNode, word):
	if trieNode is None:
		print "Dictionary is empty"
		return None
	children = trieNode.children

	for x in range(len(word)):
		print "Outer for loop"
		if len(children) <= 0:
			print word, "is not in dictionary"
			return False
		for item in children:
			print "Inner for loop"
			print "Checking if", item.char, "==", word[x]
			if word[x] == item.char:
				children = item.children
				print "breaking"
				break
			else:
				print word, "is not in dictionary"
				return False
	print word, "is in the dictionary"


def addToTrie(trieNode, word):
	if trieNode is None:
		return None
	children = trieNode.children
	for x in range(len(word)):
		notPresent = False
		for item in children:
			if word[x] == item.char:
				notPresent = True
				break
		if notPresent == False:
			newTrieNode = TrieNode(word[x])
			children.append(newTrieNode)
			children = newTrieNode.children

def printTrie(trieNode):
	if trieNode is None:
		return

	for item in trieNode.children:
		print item.char
		printTrie(item)
		trieNode = item

def initializeTrie():
	trieNode = TrieNode('0')

	return trieNode

trieNode = initializeTrie()

#searchInTrie(trieNode, "bar")
#printTrie(trieNode)
addToTrie(trieNode, "bar")
#printTrie(trieNode)
searchInTrie(trieNode, "bar")
addToTrie(trieNode, "ball")
searchInTrie(trieNode, "ball")
#printTrie(trieNode)
