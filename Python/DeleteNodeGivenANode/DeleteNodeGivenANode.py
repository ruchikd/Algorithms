class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

def deleteNode(node):
	if node is None:
		return

	if node.next is None:
		return

	node.val = node.next.val
	node.next = node.next.next


def printList(head):
	node = head
	while node != None:
		print node.val
		node = node.next

def main():
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)
	head.next.next.next.next.next = ListNode(6)
	head.next.next.next.next.next.next = ListNode(7)
	head.next.next.next.next.next.next.next = ListNode(8)

	deleteNode(head.next.next.next)
	printList(head)

if __name__ == '__main__':
	main()