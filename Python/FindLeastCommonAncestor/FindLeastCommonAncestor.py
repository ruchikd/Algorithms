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

#Complexity of below algorithm is O(h) where h = height of Tree

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
	root.left.parent = root
	root.left.left = Node(2)
	root.left.left.parent = root.left
	root.left.left.left = Node(1)
	root.left.left.left.parent = root.left.left

	root.left.right = Node(7)
	root.left.right.parent = root.left
	root.left.right.left = Node(4)
	root.left.right.left.parent = root.left.right
	root.left.right.left.left = Node(3)
	root.left.right.left.left.parent = root.left.right.left
	root.left.right.right = Node(6)
	root.left.right.right.parent = root.left.right

	root.right = Node(11)
	root.right.parent = root
	root.right.left = Node(10)
	root.right.left.parent = root.right
	root.right.right = Node (15)
	root.right.right.parent = root.right

	return root

def inorderTraversal(root):
	if root == None:
		return

	inorderTraversal(root.left)
	print root.val
	inorderTraversal(root.right)

def findLeastCommonAncestor(node1, node2):
	if node1 == None or node2 == None:
		return None

	d = dict()

	while(node1 != None):
		d[node1.val] = True
		node1 = node1.parent

	while(node2 != None):
		if node2.val in d.keys():
			return node2.val
		node2 = node2.parent

def main():
	root = createTreeAsAbove()
	#inorderTraversal(root)

	newNode = Node(50)

	lca = findLeastCommonAncestor(root.left.left.left, root.left.right.left)
	if lca == None:
		print "Either nodes are from different trees or either one of the nodes are None"
	else:
		print lca, " is least common ancestor of ", root.left.left.left.val, "and", root.left.right.left.val

	lca = findLeastCommonAncestor(root.left.left.left, newNode)
	if lca == None:
		print "Either nodes are from different trees or either one of the nodes are None"
	else:
		print lca, " is least common ancestor", root.left.left.left.val, "and", newNode.val

	lca = findLeastCommonAncestor(root.left.left.left, root)
	if lca == None:
		print "Either nodes are from different trees or either one of the nodes are None"
	else:
		print lca, " is least common ancestor", root.left.left.left.val, "and", root.val

	lca = findLeastCommonAncestor(root, root)
	if lca == None:
		print "Either nodes are from different trees or either one of the nodes are None"
	else:
		print lca, " is least common ancestor", root.val, "and", root.val

	lca = findLeastCommonAncestor(root, None)
	if lca == None:
		print "Either nodes are from different trees or either one of the nodes are None"
	else:
		print lca, " is least common ancestor", root.val, "and", None

if __name__ == '__main__':
	main()