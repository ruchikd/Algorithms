class Stack:
	def __init__(self, stackNum):
		self.stackNum = stackNum
		self.arr = []

	def push(self, stackNum, val):
		newList = []
		newList.append(val)
		newList.append(stackNum)
		self.arr.append(newList)

	def pop(self, stackNum):
		for x in reversed(xrange(len(self.arr))):
			if self.arr[x][1] == stackNum:
				self.arr.pop(x)
				break

	def peek(self, stackNum):
		for x in reversed(xrange(len(self.arr))):
			if self.arr[x][1] == stackNum:
				print self.arr[x][0]
				break

def main():
	s = Stack(3)

	s.push(1, 1)
	s.push(1, 2)
	s.push(1, 3)
	s.push(2, 4)
	s.push(1, 5)
	s.push(3, 6)
	s.push(1, 7)
	s.push(1, 8)
	s.push(2, 9)
	s.push(1, 10)
	s.push(1, 11)
	s.push(2, 12)
	s.push(2, 13)
	s.push(3, 14)

	s.pop(3)
	s.pop(1)
	s.pop(1)
	s.pop(1)

	s.peek(1)
	s.peek(2)
	s.peek(3)


if __name__=='__main__':
	main()