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

def preorderTraversal(node, bigList, smallList):
	if node is None:
		newList = []
		newList = smallList
		bigList.append(newList)
		newList = []
		if smallList:
			smallList.pop()
		return

	smallList.append(node.val)
	preorderTraversal(node.left, bigList, smallList)
	print node.val
	preorderTraversal(node.right, bigList, smallList)


def main():
	root = createTreeAsAbove()
	bigList = []
	smallList = []
	preorderTraversal(root, bigList, smallList)

	print bigList

if __name__ == '__main__':
	main()