def addNumToArr(arr, num):
	if num < 0:
		if arr == None:
			return None
		else:
			arr = []
			arr.append(num)
			return arr

	if arr == None:
		arr = []
		while num != 0:
			newNum = num%10
			arr.append(newNum)
			num = (num - newNum)/10
		return arr

	lastElementPos = len(arr)-1

	for x in reversed(xrange(len(arr))):
		if num == 0:
			break
		num = num + arr[x]
		newTemp = num%10
		arr.pop(x)
		arr.insert(x, newTemp)
		num = (num - newTemp)/10

	if num > 0:
		while True:
			if num == 0:
				break
			newTemp = num%10
			arr.insert(0, newTemp)
			num = (num - newTemp)/10

	return arr

def main():
	arr = [5,1,1]
	num = 25712

	print addNumToArr(arr, num)
	print 511 + 25712

if __name__ == '__main__':
	main()