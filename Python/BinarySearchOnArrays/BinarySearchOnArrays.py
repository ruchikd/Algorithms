def binSearch(arr, start, end, val):
	mid = (start+end)/2
	if end - start <= 1:
		print "Value is not presetn"
		return None
	if arr[mid] == val:
		print "val =", val, "is located at index", mid
		return mid
	elif arr[mid] > val:
		binSearch(arr, start, mid, val)
	else:
		binSearch(arr, mid, end, val)

def main():
	arr = [5,237,3,5,7,34,7,45,7,37,37,86,44,45,7,43,5,7,8,6,3,5,26,]
	print sorted(arr)
	binSearch(sorted(arr), 0, len(arr), 37)

if __name__ == '__main__':
	main()