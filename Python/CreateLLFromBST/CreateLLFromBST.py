#**************************************************************
#                          9
#                        /   \
#                      5       11
#                   /    \      / \
#                  2      7    10  15
#                /       / \
#               1       4    6
#                      /
#                     3
#**************************************************************

class Node:
	val, left, right, parent = None, None, None, None

	def __init__ (self, val):
		self.val = val
		self.left = None
		self.right = None

def createTreeAsAbove():
	root = Node(9)
	
	root.left = Node(5)
	root.left.left = Node(2)
	root.left.left.left = Node(1)

	root.left.right = Node(7)
	root.left.right.left = Node(4)
	root.left.right.left.left = Node(3)
	root.left.right.right = Node(6)

	root.right = Node(11)
	root.right.left = Node(10)
	root.right.right = Node (15)

	return root

def getHeight(node):
	if node is None:
		return 0

	lHeight = getHeight(node.left)
	rHeight = getHeight(node.right)

	if(lHeight > rHeight):
		return lHeight + 1
	else:
		return rHeight + 1

def getList(node, height, list):
	if node is None:
		return

	if height == 0:
		list.append(node.val)
	else:
		getList(node.left, height-1, list)
		getList(node.right, height-1, list)

	return list

def levelOrderTraversal(node):
	height = getHeight(node)

	list = []

	for x in range(height):
		getList(node, x, list)

	print list

def main():
	root = createTreeAsAbove()

	levelOrderTraversal(root)

if __name__ == '__main__':
	main()