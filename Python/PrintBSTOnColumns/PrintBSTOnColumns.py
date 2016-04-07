#                 4
#               /   \
#              2     6
#            /  \   /  \
#           1    3  5   7

#                 4
#               /   \
#              2     2
#            /  \   /  \
#           1    3  3   1

class Node:
	rChild, lChild, data = None, None, None

	def __init__(self, data):
		self.rChild = None
		self.lChild = None
		self.data = data

def inorder(root):
	if root is None:
		return

	inorder(root.lChild)
	print root.data
	inorder(root.rChild)

def fillCoordinates(root,x, y, coordinateList):
	if root is None:
		return

	fillCoordinates(root.lChild, x-1, y-1, coordinateList)
	localList = []
	localList.append(x)
	localList.append(y)
	localList.append(root.data)
	coordinateList.append(localList)
	fillCoordinates(root.rChild, x+1, y-1, coordinateList)

def printBSTColumnWise(root, coordinateList):
	fillCoordinates(root, 0, 0, coordinateList)

	arr = []
	gen = (x for x in coordinateList)
	start = min(x[0] for x in gen)
	diff = 0 - start
	for coordinates in coordinateList:
		val = coordinates[0]
		newVal = val + diff
		coordinates[0] = newVal

	maxLen = coordinateList[len(coordinateList)-1][0]
	sumList = []
	for x in range(maxLen+1):
		sumList.append(0)

	for coordinates in coordinateList:
		sumList[coordinates[0]] = sumList[coordinates[0]] + coordinates[2]

	print sumList

def main():
	root = Node(4)
	root.lChild = Node(2)
	root.rChild = Node(2)
	root.lChild.lChild = Node(1)
	root.lChild.rChild = Node(3)
	root.rChild.lChild = Node(3)
	root.rChild.rChild = Node(1)

	#inorder(root)

	coordinateList = []
	printBSTColumnWise(root, coordinateList)

if __name__ == '__main__':
	main()