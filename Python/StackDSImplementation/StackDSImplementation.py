class stack:
	def __init__ (self):
		self.items = []

	def push(self, val):
		self.items.append(val)

	def pop(self):
		if not self.items:
			return -1
		return self.items.pop()

	def peek(self):
		val = self.pop()
		self.push(val)
		return val

	def size(self):
		return len(self.items)

def main():
	s = stack()

	for x in range(1, 10):
		s.push(x)

	print s.peek()
	s.push(15)
	print s.peek()
	s.pop()
	print s.peek()
	s.pop()
	print s.size()
	print s.peek()
	s.push(12)
	print s.peek()
	print s.size()

if __name__ == '__main__':
	main()