class Node:
	def __init__(self, val, next):
		self.val = val
		self.next = next

def printAllLL(n):
	if n is None:
		return

	print n.val
	printAllLL(n.next)

def findNthElement(node, n):
	p1 = node
	p2 = node
	iter = 0

	'''
	for x in range(n-1):
		p1 = p1.next

	while p1.next is not None:
		p1 = p1.next
		p2 = p2.next

	print p2.val
	'''
	while p1.next is not None:
		if iter >= n-1:
			p1 = p1.next
			p2 = p2.next
		else:
			iter = iter + 1
			p1 = p1.next

	print p2.val
	#'''

n8 = Node(8, None)
n7 = Node(7, n8)
n6 = Node(6, n7)
n5 = Node(5, n6)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n0 = Node(0, n1)

#printAllLL(n0)
findNthElement(n0, 5)