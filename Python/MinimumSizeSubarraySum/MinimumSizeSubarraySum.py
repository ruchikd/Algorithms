import sys

def findMinimumSizeSubarraySum(a, s):
	i, j, sumN, minN = 0, 0, 0, sys.maxsize

	while j < len(a):
		sumN = sumN + a[j]
		j = j + 1

		while (sumN >= s):
			minN = min(minN, j - i)
			sumN = sumN - a[i]
			i = i + 1

	return minN

def main():
	arr = [ 2, 1, 3, 4, 0, -9, -7, 8]
	val = 7

	print findMinimumSizeSubarraySum(arr, val)

if __name__ == '__main__':
	main()