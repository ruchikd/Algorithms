def get3Sum(arr):
	nums = sorted(arr)
	mainList = []

	for i in range(len(arr)-2):
		if (i > 0) and (nums[i] == nums[i-1]):
			continue
		j = i + 1
		k = len(nums) -1
		while (j < k):
			if (nums[i] + nums[j] + nums[k] == 0):
				innerList = []
				innerList.append(nums[i])
				innerList.append(nums[j])
				innerList.append(nums[k])
				mainList.append(innerList)
				j = j + 1
				k = k - 1
				while (j < k) and (nums[j] == nums[j-1]):
					j = j + 1
				while (j < k) and (nums[k] == nums[k+1]):
					k = k - 1
			elif (nums[i] + nums[j] + nums[k] > 0):
				k = k - 1
			else:
				j = j + 1

	return mainList

def main():
	arr = [2, 1, 3, 4, 0, -9, -9, -7, 8]
	print get3Sum(arr)

if __name__ == '__main__':
	main()