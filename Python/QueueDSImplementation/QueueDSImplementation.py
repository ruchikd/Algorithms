class queue:
	def __init__(self):
		self.items = []

	def enqueue(self, val):
		self.items.insert(0, val)
		return True

	def dequeue(self):
		return self.items.pop()

	def peek(self):
		val = self.dequeue()
		pos = self.size()
		self.items.insert(pos, val)
		return val

	def size(self):
		return (len(self.items))

def main():
	q = queue()

	for x in range(15):
		q.enqueue(x)

	print q.size()
	print q.peek()
	print q.peek()

if __name__ == '__main__':
	main()