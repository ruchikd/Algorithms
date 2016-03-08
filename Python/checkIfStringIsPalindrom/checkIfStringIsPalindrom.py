def checkIfPalindrom(oriStr):
	length = len(oriStr)

	for x in range(len(oriStr)):
		if oriStr[length-1-x] != oriStr[x]:
			print "String is not a palindrom"
			return

	print "String is palindrom"

def main():
	oriStr = 'abcddcbaa'
	checkIfPalindrom(oriStr)

if __name__ == '__main__':
	main()