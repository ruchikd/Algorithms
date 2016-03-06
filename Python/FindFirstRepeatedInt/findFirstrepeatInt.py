arr = [1,2,3,4,5,5,6,7,8,9,0,0]

def findFirstOccurance():
	intDict = {}
	for i in arr:
		if i not in intDict:
			intDict[i] = 'set'
		else:
			return i

def main():
	print arr
	i = findFirstOccurance()
	print i

if __name__ == '__main__':
	main()