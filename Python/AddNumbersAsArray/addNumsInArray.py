def getNumFromArray(arr):
	length = len(arr)
	tens = 1
	num = 0

	for i in range(len(arr) -1, -1, -1):
		try:
			int(arr[i])
		except ValueError:
			return -1
		num = num + (int(arr[i]) * tens)
		tens = tens *  10

	return num

def addArrays(arr1, arr2, arr3):
	num1 = getNumFromArray(arr1)
	if num1 is -1:
		print "Error in first array"
		num1 = 0
	num2 = getNumFromArray(arr2)
	if num2 is -1:
		print "Error in second array"
		num2 = 0
	num3 = getNumFromArray(arr3)
	if num3 is -1:
		print "Error in second array"
		num3 = 0

	num = num1 + num2 + num3

	print num

def main():
	num1 = ("2", "4", "6")
	num2 = ("1")
	num3 = ("5", "3", "8", "2", "9")

	addArrays(num1, num2, num3)

if __name__ == '__main__':
	main()