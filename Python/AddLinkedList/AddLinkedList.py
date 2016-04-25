class Node:
	def __init__(self, val, next):
		self.val = val
		self.next = next

def printAllLL(n):
	if n is None:
		return

	print n.val
	printAllLL(n.next)

def addLinkedList(l1, l2):
	num1, num2 = 0, 0

	if l1 is not None:
		iter = 0
		while l1 is not None:
			print "l1.val = ", l1.val
			num1 = num1 + (l1.val*(10**iter))
			print "num1 =", num1
			l1 = l1.next
			iter = iter + 1

	if l2 is not None:
		iter = 0
		while l2 is not None:
			num2 = num2 + (l2.val*(10**iter))
			l2 = l2.next
			iter = iter + 1

	newNum = num1 + num2
	print num1, num2, newNum

	previous = None
	num = 0
	while (newNum != 0):
		num = newNum%10
		n = Node(num, previous)
		previous = n
		newNum = (newNum - num)/10
		n = n.next

n7 = Node(2, None)
n6 = Node(9, n7)
n5 = Node(5, n6)
n2 = Node(5, None)
n1 = Node(1, n2)
n0 = Node(3, n1)

addLinkedList(n0, n5)