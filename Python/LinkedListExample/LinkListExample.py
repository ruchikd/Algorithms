class Node:
	data, next = None, None
	def __init__ (self, val):
		self.val = val
		self.next = None

def appendToLinkList(start, val):
	nextNode = Node(val)

	if (start == None):
		start = nextNode
		return start

	node = start
	while (node.next != None):
		node = node.next

	node.next = nextNode

	return start

def addBetweenLinkList(node, val, afterVal):
	if (node == None):
		return None

	addNode = Node(val)

	while (node.next != None):
		if (node.val == afterVal):
			nextNode = node.next
			node.next = addNode
			addNode.next = nextNode
		node = node.next

def delFromLinkList(start, val):
	if (start == None):
		return None

	if (start.val == val):
		while (start.next != None):
			if (start.val != val):
				break
			nodeToDelete = start
			start = start.next
			nodeToDelete = None

	node = start
	while(node.next != None):
		if (node.next.val == val):
			nodeToDelete = node.next
			if (nodeToDelete.next != None):
				node.next = node.next.next
			nodeToDelete = None
		node = node.next

	return start

def main():
	start = None

	for i in range(100):
		start = appendToLinkList(start, i)

	addBetweenLinkList(start, 111, 90)

	start = delFromLinkList(start, 98)

	node = start
	while (node.next != None):
		print node.val
		node = node.next

if __name__ == '__main__':
	main()