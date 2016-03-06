
arr = [1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1]

def findLongestStreak(k):
	onesCount = 0
	zeroCount = 0
	longestStreak = 0

	for x in range(len(arr)):
		if arr[x] == 0:
			if zeroCount == k:
				if (onesCount > longestStreak):
					longestStreak = onesCount

def main():
	findLongestStreak()

if __name__ == '__main__':
	main()