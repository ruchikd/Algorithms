# 0 1 1 2 3 5 8 13 21 34 ...
# n + (n+1)

def printFibonacci(n, m, val):
	if val == 0:
		return

	print n
	val = val - 1
	printFibonacci(m, n+m, val)

def returnNthFiboNum(val):
	if val == 0:
		return 0
	elif val == 1:
		return 1
	elif val > 1:
		return returnNthFiboNum(val-1) + returnNthFiboNum(val-2)
	else:
		return -1

def main():
	printFibonacci(0, 1, 16)
	print ""
	print returnNthFiboNum(15)

if __name__ == '__main__':
	main()