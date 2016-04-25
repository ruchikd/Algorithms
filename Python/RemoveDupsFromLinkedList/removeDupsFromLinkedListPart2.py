class Node:
	def __init__(self, val, next):
		self.val = val
		self.next = next

def printAllLL(n):
	if n is None:
		return

	print n.val
	printAllLL(n.next)

def removeDups(n):
	if n is None:
		return

	d = dict()

	previous = None
	while n is not None:
		if n.val in d.keys():
			previous.next = n.next
		else:
			d[n.val] = True
			previous = n
		n = n.next

n8 = Node(8, None)
n7 = Node(7, n8)
n6 = Node(6, n7)
n5 = Node(5, n6)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n0 = Node(0, n1)

printAllLL(n0)
removeDups(n0)
print ""
printAllLL(n0)