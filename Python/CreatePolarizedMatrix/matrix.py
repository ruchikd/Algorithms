num = 2

matrixDimensions = (num*2) - 1

"""
5 = 9
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555

3 = 5
33333
32223
32123
32223
33333

2 = 3
222
212
222
"""

Matrix = [[0 for x in range (matrixDimensions)] for x in range (matrixDimensions)]

print Matrix

print matrixDimensions
row = 0

for x in range (matrixDimensions):
	row += 1
	Matrix[x][y] = row

print Matrix
