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

	fillCoordinates(root.lChild, x-1, y+1, coordinateList)
	localList = []
	localList.append(x)
	localList.append(y)
	localList.append(root.data)
	coordinateList.append(localList)
	fillCoordinates(root.rChild, x+1, y+1, coordinateList)

def getXKey(item):
	return item[0]

def getYKey(item):
	return item[1]

def sort(coordinateList):
	sortedListVal = []

	sorted(coordinateList, key=getXKey)
	#sorted(coordinateList, key=getYKey)

	for coordinates in coordinateList:
		print coordinates

def printBSTColumnWise(root, coordinateList):
	fillCoordinates(root, 0, 0, coordinateList)

	sort(coordinateList)

	print coordinateList

def main():
	root = Node(4)
	root.lChild = Node(2)
	root.rChild = Node(6)
	root.lChild.lChild = Node(1)
	root.lChild.rChild = Node(3)
	root.rChild.lChild = Node(5)
	root.rChild.rChild = Node(7)

	#inorder(root)

	coordinateList = []
	printBSTColumnWise(root, coordinateList)

if __name__ == '__main__':
	main()