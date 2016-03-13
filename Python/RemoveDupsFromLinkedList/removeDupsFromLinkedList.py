class Node:
	def __init__ (self, val):
		self.val = val
		self.next = None

def printList(list):
	if list is None:
		print "Empty list"
		return

	while list != None:
		print list.val
		list = list.next

def addToList(list, val):
	if list is None:
		print "Empty list"
		return

	while list != None:
		if list.val == val:
			newList = Node(val)
			if list.next is None:
				list.next = newList
			else:
				newList.next = list.next
				list.next = newList
			list = newList.next
		else:
			list = list.next

def findAndRemoveDups(head):
	previous = None
	list = head
	if list is None:
		print "Empty list"
		return

	d = dict()

	while list != None:
		if list.val in d.keys():
			previous.next = list.next
		else:
			d[list.val] = True
			previous = list
		list = list.next

def main():
	head = Node(0)
	temp = head

	for x in range(1, 100):
		tempNext = Node(x)
		temp.next = tempNext
		temp = tempNext

	#printList(head)
	addToList(head, 0)
	#printList(head)
	findAndRemoveDups(head)
	printList(head)

if __name__ == '__main__':
	main()