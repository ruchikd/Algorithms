def threeSumClosest(nums):
	if (len(nums)) < 3:
		return

	biglist = []
	sortedList = sorted(nums)

	for x in range(len(sortedList)):
		for y in range(x+1, len(sortedList)):
			for z in range(y+1, len(sortedList)):
				sumNums = sortedList[x] + sortedList[y] + sortedList[z]
				if (sumNums == 0) and (sortedList[x] <= sortedList[y] <= sortedList[z]):
					smallList = []
					smallList.append(sortedList[x])
					smallList.append(sortedList[y])
					smallList.append(sortedList[z])
					biglist.append(smallList)

	return biglist

def main():
	arr = [-1, 0, 1, 2, -1, -4]

	print threeSumClosest(arr)

if __name__ == '__main__':
	main()