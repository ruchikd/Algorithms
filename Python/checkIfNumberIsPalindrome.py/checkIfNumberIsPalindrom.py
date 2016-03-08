def checkIfNumIsPalindrom(num):
	newNum = 0
	temp = num

	while (temp != 0):
		newNum = (newNum * 10) + (temp%10)
		temp = (temp-(temp%10))/10

	print newNum

	if (num - newNum) == 0:
		print "Given num is palindrom"
	else:
		print "Given num is not a palindrom"

def main():
	num = 1234321

	checkIfNumIsPalindrom(num)

if __name__ == '__main__':
	main()