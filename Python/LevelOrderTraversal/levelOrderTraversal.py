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

from Queue import *

class Node:
	val, left, right, parent = None, None, None, None

	def __init__ (self, val):
		self.val = val
		left = None
		right = None
		parent = None

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

def height(root):
	if root is None:
		return 0

	lheight = height(root.left)
	rheight = height(root.right)

	if(lheight > rheight):
		return lheight + 1
	else:
		return rheight + 1

def printLevelOrder(root, height):
	if root is None:
		return
	elif height == 1:
		print root.val
	elif height > 1:
		printLevelOrder(root.left, height-1)
		printLevelOrder(root.right, height-1)

def levelOrderTraversal(root):
	h = height(root)

	for i in range(1, h+1):
		printLevelOrder(root, i)

def main():
	root = createTreeAsAbove()

	levelOrderTraversal(root)

if __name__ == '__main__':
	main()