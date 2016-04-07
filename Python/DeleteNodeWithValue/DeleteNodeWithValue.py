class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

def printList(head):
	node = head
	while node != None:
		print node.val
		node = node.next

def removeElements(head, val):
	if head is None:
		return

	while head != None:
		if head.val != val:
			break
		temp = head
		head = head.next
		del temp

	if head == None:
		return

	node = head

	while node.next != None:
		if node.next.val == val:
			temp = node.next
			node.next = node.next.next
			del temp
		else:
			node = node.next

	printList(head)
	i = 10
	update(i)
	print i
	return head

def update(i):
	i = 5

def main():
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(2)
	head.next.next.next.next = ListNode(5)
	head.next.next.next.next.next = ListNode(6)
	head.next.next.next.next.next.next = ListNode(2)
	head.next.next.next.next.next.next.next = ListNode(8)

	removeElements(head, 1)

if __name__ == '__main__':
	main()