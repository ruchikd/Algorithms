def get3Sum(arrList):
	nums = sorted(arrList)
	threeSumList = []

	for i in range(len(nums)-2):
		if (nums[i] == 0):
			innerList = []
			innerList.append(nums[i])
			innerList.append(nums[i])
			innerList.append(nums[i])
			threeSumList.append(innerList)
		if (i > 0) and (nums[i] == nums[i-1]):
			continue
		j = i + 1
		k = len(nums) - 1
		while j < k:
			if (nums[i] + nums[j] + nums[k] == 0):
				innerList = []
				innerList.append(nums[i])
				innerList.append(nums[j])
				innerList.append(nums[k])
				threeSumList.append(innerList)
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

	return threeSumList


def main():
	arrList = [-1,0,1,2,-1,-4]

	print get3Sum(arrList)

if __name__ == '__main__':
	main()