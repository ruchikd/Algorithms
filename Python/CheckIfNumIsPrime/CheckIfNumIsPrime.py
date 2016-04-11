def checkIfNumIsPrime(num):
	for x in xrange(2, num):
		if num%x == 0:
			return num, "is not Prime"

	return num, "is Prime"

def main():
	print checkIfNumIsPrime(3)
	print checkIfNumIsPrime(9)
	print checkIfNumIsPrime(27)
	print checkIfNumIsPrime(23)

if __name__ == '__main__':
	main()