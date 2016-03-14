class Node:
	def __init__(self, val):
		self.val = val
		self.lChild = None
		self.rChild = None

def addToTree(arr, start, end):
	if (end < start):
		return None

	mid = (start+end)/2
	n = Node(mid)
	n.val = arr[mid]

	n.lChild = addToTree(arr, start, mid - 1)
	n.rChild = addToTree(arr, mid + 1, end)

	return n

def inorderT(node):
	if node is None:
		return

	inorderT(node.lChild)
	print node.val
	inorderT(node.rChild)

def main():
	arr = (1,2,3,4,5,6,7,8,9,10)
	root = addToTree(arr, 0, 9)

	inorderT(root)

if __name__ == '__main__':
	main()