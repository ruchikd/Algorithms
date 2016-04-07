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

def rightInorder(root, rightList):
	if root is None:
		return

	rightInorder(root.rChild, rightList)
	rightList.append(root.data)
	rightInorder(root.lChild, rightList)

def leftInorder(root, leftList):
	if root is None:
		return

	leftInorder(root.lChild, leftList)
	leftList.append(root.data)
	leftInorder(root.rChild, leftList)

def isBSTMirror(root):
	leftList = []
	rightList = []

	leftInorder(root, leftList)
	rightInorder(root, rightList)

	print leftList
	print rightList

	if leftList == rightList:
		print "BST is mirror"
	else:
		print "BST is not mirrot"

def main():
	root = Node(4)
	root.lChild = Node(2)
	root.rChild = Node(2)
	root.lChild.lChild = Node(1)
	root.lChild.rChild = Node(3)
	root.rChild.lChild = Node(3)
	root.rChild.rChild = Node(1)

	inorder(root)

	isBSTMirror(root)

if __name__ == '__main__':
	main()