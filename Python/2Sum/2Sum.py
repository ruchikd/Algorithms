def find2Sum(arr, target):
	if arr is None:
		return None

	sumList = []
	d = dict()

	for x in range(len(arr)):
		if arr[x] in d:
			index = d[arr[x]]
			smallList = []
			smallList.append(index)
			smallList.append(x)
			sumList.append(smallList)
		else:
			d[target - arr[x]] = x

	print sumList

def main():
	arr = [2, 7, 11, 15]
	target = 9

	find2Sum(arr, target)

if __name__ == '__main__':
	main()