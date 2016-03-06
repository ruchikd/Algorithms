def findDup(arr, distance):
	for i in range(len(arr)):
		start = i
		end = i+distance
		for j in arr[start:end]:
			if arr[i] == arr[j]:
				print arr[i]

def main():
	arr = (1, 2, 4, 5, 3, 9, 8, 3, 5, 6, 2)

	findDup(arr, 3)

if __name__ == '__main__':
	main()