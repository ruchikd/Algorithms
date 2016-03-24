class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

def oddEvenList(head):
        if head == None:
            return None
            
        oddHead, oddNode, evenHead, evenNode = None, None, None, None
        
        oddHead = ListNode(head.val)
        oddNode = oddHead
        evenHead = ListNode(head.next.val)
        evenNode = evenHead
        
        if (head.next == None):
            return head
        
        if (head.next.next == None):
            return head
            
        head = head.next.next
        i = 1
        print head.val
            
        while True:
        	if head == None:
        		break
        	if i%2 != 0:
        		newNode = ListNode(head.val)
        		oddNode.next = newNode
        		oddNode = oddNode.next
        	else:
        		newNode = ListNode(head.val)
        		evenNode.next = newNode
        		evenNode = evenNode.next
        	i = i +1
        	head = head.next

        oddNode.next = evenHead
        return oddHead

def printList(head):
	node = head
	while node != None:
		print node.val
		node = node.next

def main():
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	'''
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)
	head.next.next.next.next.next = ListNode(6)
	head.next.next.next.next.next.next = ListNode(7)
	head.next.next.next.next.next.next.next = ListNode(8)
	'''

	head = oddEvenList(head)
	print ""
	printList(head)

if __name__ == '__main__':
	main()