def moveZeroes(nums, val):
	if nums is None or len(nums) <= 1:
		return nums

	for x in range(len(nums)):
		if nums[x] == val:
			for y in range(x, len(nums)):
				if nums[y] != val:
					temp = nums[y]
					nums[y] = nums[x]
					nums[x] = temp
					break

	length = 0
	for x in range(len(nums)):
		if nums[x] == val:
			break
		length = length+1

	print nums

	return length

def main():
	nums = [3, 2, 2, 3]
	print nums
	val = 3

	print moveZeroes(nums, val)

if __name__ == '__main__':
	main()