def addNumToArr(arr, num):
	newNum = 0
	for x in xrange(len(arr)):
		newNum = newNum*10 + arr[x]

	arrNum = newNum + num
	arr = []

	while True:
		if arrNum == 0:
			break
		num = arrNum%10
		arr.insert(0, num)
		arrNum = (arrNum - num)/10

	return arr

def main():
	arr = [5,1,1]
	num = 12

	print addNumToArr(arr, num)
	print 511 + 25712

if __name__ == '__main__':
	main()