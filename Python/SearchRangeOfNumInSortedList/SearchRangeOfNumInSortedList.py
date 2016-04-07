def searchRange(nums, target):
    start = 0
    end = len(nums) - 1

    rangeList = []
    rangeList.append(-1)
    rangeList.append(-1)

    if len(nums) <= 0:
        return rangeList

    while True:
        if start >= end:
            break

        if (end - start) < 2:
            break

        print end
        if target > nums[end]:
            break

        if (nums[(start+end)/2] > target):
            start = (start+end)/2
        else:
            end = (start+end)/2

    return rangeList

def main():
	nums = [1, 2, 3]
	target = 1

	print searchRange(nums, target)

if __name__ == '__main__':
	main()