def moveZeroes(arr):
	if arr is None or len(arr) <= 1:
		return arr

	for x in range(len(arr)):
		if arr[x] == 0:
			for y in range(x, len(arr)):
				if arr[y] != 0:
					temp = arr[y]
					arr[y] = arr[x]
					arr[x] = temp
					break

	return arr

def main():
	arr = [0, 1, 0, 3, 12]
	print arr

	print moveZeroes(arr)

if __name__ == '__main__':
	main()