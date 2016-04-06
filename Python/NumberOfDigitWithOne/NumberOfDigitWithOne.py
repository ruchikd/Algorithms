def retNumOfDigitsWithOne(num):
	if num <= 0:
		return 0

	totalNumsWith1s = 0

	for n in xrange(num+1):
		while n != 0:
			if (n%10) == 1:
				totalNumsWith1s = totalNumsWith1s + 1
			n = (n - (n%10))/10

	return totalNumsWith1s

def main():
	num = 3184191

	print retNumOfDigitsWithOne(num)

if __name__ == '__main__':
	main()