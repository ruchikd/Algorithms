class Node:
	def __init__ (self, val, next):
		self.val = val
		self.next = next

def printNodes(n):
	if n is None:
		return
	print n.val
	printNodes(n.next)

def recursiveReverse(n, last):
	if n is None:
		return

	next = n.next
	n.next = last
	recursiveReverse(next, n)

n7 = Node(7, None)
n6 = Node(6, n7)
n5 = Node(5, n6)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n0 = Node(0, n1)

print ""
printNodes(n0)
recursiveReverse(n0, None)
print ""
printNodes(n7)