##################
#    0 1 2 3 4
#0 [[x,0,0,0,x],
#1  [0,0,x,0,0],
#2  [x,0,x,0,0],
#3  [x,0,0,0,x],
#4  [0,0,x,0,0]]
##################
#In above case there are 4 islands - 
# x then x then x,x then x
#        x      x

#islands =  [[1,0,0,0,1], [0,0,1,0,0], [1,0,1,0,0], [1,0,0,0,1], [0,0,1,0,0]]
islands =  [[1,0,0,0,0], [0,0,0,0,0], [1,0,1,1,0], [0,0,0,0,0], [1,0,0,1,0]]

def findIslands():
	numOfIslands = 0

	for i in range(len(islands)):
		for j in range(len(islands[i])):
			if islands[i][j] == 1:
				if i == 0 and j == 0:
					numOfIslands += 1
					continue

				if (islands[i-1][j] != 1) and (islands[i][j-1] != 1) and (islands[i-1][j-1] != 1):
					numOfIslands += 1

	print "Total number of islands = ", numOfIslands

def main():
	findIslands()

if __name__ == '__main__':
	main()