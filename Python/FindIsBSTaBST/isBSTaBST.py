#                 4
#               /   \
#              2     6
#            /  \   /  \
#           1    3  5   7

class Node:
	rChild, lChild, data = None, None, None

	def __init__(self, data):
		self.rChild = None
		self.lChild = None
		self.data = data

INT_MIN = -4294967296
INT_MAX = 4294967296

def inorder(root):
	if root is None:
		return

	inorder(root.lChild)
	print root.data
	inorder(root.rChild)

def isBSTUtil(node, min, max):
	if node is None:
		return True

	if node.data < min or node.data > max:
		return False

	return (isBSTUtil(node.lChild, min, node.data - 1) and isBSTUtil(node.rChild, node.data + 1, max))

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
	if isBSTUtil(root, INT_MIN, INT_MAX) == False:
		print "Not a BST"

if __name__ == '__main__':
	main()