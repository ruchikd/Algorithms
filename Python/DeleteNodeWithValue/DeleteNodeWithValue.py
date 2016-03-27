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

	while True:
		if head.val == val:
			head = head.next
		else:
			break
		if head is None:
			break
	node = head

	while True:
		if node == None:
			break
		if node.next == None:
			break
		if node.next.val == val:
			node.next = node.next.next
			node = node.next.next
			if node == None:
				break
		else:
			node = node.next

	return head

def main():
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(2)
	head.next.next.next.next = ListNode(5)
	head.next.next.next.next.next = ListNode(6)
	head.next.next.next.next.next.next = ListNode(2)
	head.next.next.next.next.next.next.next = ListNode(8)

	removeElements(head, 2)
	printList(head)

if __name__ == '__main__':
	main()