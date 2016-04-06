#                 4
#               /   \
#              2     6
#            /  \   /  \
#           1    3  5   7
import sys

class Node:
	rChild, lChild, data = None, None, None

	def __init__(self, data):
		self.rChild = None
		self.lChild = None
		self.data = data

INT_MIN = -sys.maxint
INT_MAX = sys.maxint

def inorder(root):
	if root is None:
		return

	inorder(root.lChild)
	print root.data
	inorder(root.rChild)

def isBSTUtil(root, min, max):
	if root is None:
		return True

	if root.data < min or root.data > max:
		return False

	return (isBSTUtil(root.lChild, min, root.data - 1) and isBSTUtil(root.rChild, root.data + 1, max))

def main():
	root = Node(4)
	root.lChild = Node(2)
	root.rChild = Node(6)
	root.lChild.lChild = Node(1)
	root.lChild.rChild = Node(3)
	root.rChild.lChild = Node(5)
	root.rChild.rChild = Node(7)

	inorder(root)

	if isBSTUtil(root, INT_MIN, INT_MAX) == True:
		print "Is BST"
	else:
		print "Is not BST"

if __name__ == '__main__':
	main()