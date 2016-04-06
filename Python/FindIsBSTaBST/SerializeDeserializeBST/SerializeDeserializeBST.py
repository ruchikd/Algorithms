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

def inorder(root):
	if root is None:
		print "root is None"
		return

	inorder(root.lChild)
	print root.data
	inorder(root.rChild)

def serializeTree(root, treeList):
	if root is None:
		treeList.append(None)
		return

	treeList.append(root.data)
	serializeTree(root.lChild, treeList)
	serializeTree(root.rChild, treeList)

def deserializeTree(newRoot, treeList, pos):
	if treeList[pos] == None or pos == len(treeList):
		return
	print "asigning newRoot with value:", treeList[pos], "at position", pos
	newRoot = Node(treeList[pos])

	pos = pos + 1
	deserializeTree(newRoot.lChild, treeList, pos)
	pos = pos + 1
	deserializeTree(newRoot.rChild, treeList, pos)

def main():
	root = Node(4)
	root.lChild = Node(2)
	root.rChild = Node(6)
	root.lChild.lChild = Node(1)
	root.lChild.rChild = Node(3)
	root.rChild.lChild = Node(5)
	root.rChild.rChild = Node(7)

	#inorder(root)

	treeList = []
	serializeTree(root, treeList)
	print treeList

	newRoot = None
	deserializeTree(newRoot, treeList, 0)

	inorder(newRoot)

if __name__ == '__main__':
	main()