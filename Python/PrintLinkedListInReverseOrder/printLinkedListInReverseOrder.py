#######################
# 1-2-3-4-5-6-7-8-9-10
#######################

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def createList():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)
	head.next.next.next.next.next = Node(6)
	head.next.next.next.next.next.next = Node(7)
	head.next.next.next.next.next.next.next = Node(8)
	head.next.next.next.next.next.next.next.next = Node(9)
	head.next.next.next.next.next.next.next.next.next = Node(10)

	return head

def printReverseList(head):
	if head == None:
		return
	else:
		printReverseList(head.next)
		print head.val

def main():
	head = createList()

	#recursive method
	printReverseList(head)

	#iterative method
	linkList = []
	while True:
		if head is None:
			break
		linkList.append(head.val)
		head = head.next

	while True:
		if len(linkList) > 0:
			print linkList.pop()

if __name__ == '__main__':
	main()