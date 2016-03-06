class Node:
	rChild, lChild, data = None, None, None

	def __init__(self, data):
		self.rChild = None
		self.lChild = None
		self.data = data

def insert(root, val):
	if root is None:
		root = Node(val)
	elif root.data > val:
		if root.lChild is None:
			root.lChild = Node(val)
		else:
			insert(root.lChild, val)
	else:
		if root.rChild is None:
			root.rChild = Node(val)
		else:
			insert(root.rChild, val)

def inorder(root):
	if root is None:
		return

	inorder(root.lChild)
	print root.data
	inorder(root.rChild)


def main():
	root = Node(4)
	insert(root, 1)
	insert(root, 3)
	insert(root, 5)
	insert(root, 2)
	insert(root, 6)

	inorder(root)


if __name__ == '__main__':
	main()