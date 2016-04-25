MAX = 3

class Stack:
	def __init__ (self):
		self.stacks = []

	def push(self, val):
		newStack = False
		if len(self.stacks) == 0:
			stack = []
			stack.append(val)
			self.stacks.append(stack)
			return

		for stack in self.stacks:
			if len(stack) == MAX:
				continue
			elif len(stack) < MAX:
				stack.append(val)
				return

		stack = []
		stack.append(val)
		self.stacks.append(stack)

	def pop(self):
		for stack in self.stacks:
			if len(stack) == MAX:
				continue
			ret = 0
			print "len(stack) =", len(stack)
			if 0 < len(stack) < MAX:
				print stack
				ret = stack.pop()
				print stack
			if len(stack) == 0:
				print "len of stack is 0"
				del stack
				print self.stacks

			return ret

	def printAllStacks(self):
		print self.stacks

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)

s.printAllStacks()

print s.pop()
s.printAllStacks()
print s.pop()
s.printAllStacks()
print s.pop()
s.printAllStacks()