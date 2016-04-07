def findIfPowOf3(num):
	newNum = num%3
	if newNum == 0:
		newNum = num/3
	else:
		print "Num not power of 3"
		return False
	secNum = newNum%3
	if secNum == 0:
		secNum = newNum/3
	else:
		print "Num not power of 3"
		return False

	return secNum

def main():
	print findIfPowOf3(27)
	print findIfPowOf3(-27)

if __name__ == '__main__':
	main()