###############################
#   1,  2,  3,  4
#   5,  6,  7,  8
#   9, 10, 11, 12
#  13, 14, 15, 16
################################

def printMatrix(matrix):
	if matrix is None:
		return
		
	for x in matrix:
		print x
	print ""

def getZeroInfo(matrix):
	if matrix is None:
		return

	rowList = []
	colList = []

	for m in range(4):
		for n in range(4):
			if matrix[m][n] == 0:
				rowList.append(n)
				colList.append(m)

	return rowList, colList

def makeMatrixZero(matrix, rowList, colList):
	if matrix is None:
		return

	for m in range(4):
		for n in range(4):
			if m in colList:
				matrix[m][n] = 0
			if n in rowList:
				matrix[m][n] = 0

def main():
	matrix = [ [ 0 for i in range(4) ] for j in range(4) ]
	printMatrix(matrix)

	i = 1
	print ""
	for m in range(4):
		for n in range(4):
			matrix[m][n] = i;
			i += 1

	printMatrix(matrix)
	#matrix[3][3] = 0
	#printMatrix(matrix)

	rowList, colList = getZeroInfo(matrix)
	print rowList
	print colList
	print ""

	makeMatrixZero(matrix, rowList, colList)
	printMatrix(matrix)

if __name__ == '__main__':
	main()