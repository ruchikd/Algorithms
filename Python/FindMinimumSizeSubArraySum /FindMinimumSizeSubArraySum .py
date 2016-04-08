def finMinSizeSubArraySize(arr, x):

	currSum = 0
	minLen = len(arr)+1

	start, end = 0, 0
	n = len(arr)

	while (end < n):
		while (currSum <= x) and (end < n):
			currSum = currSum + arr[end]
			end = end + 1
		while (currSum > x) and (start < n):
			if (end - start < minLen):
				minLen = end - start

			currSum = currSum - arr[start]
			start = start + 1

	return minLen

def main():
	arr = [1, 4, 45, 6, 10, 192,3,1,5,12,66,22,5,78]
	x = 51

	print finMinSizeSubArraySize(arr, x)

if __name__ == '__main__':
	main()