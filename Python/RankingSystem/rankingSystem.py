class Students:
	def __init__ (self, name, percentage):
		self.name = name
		self.percentage = percentage

def getPercentile(percentageList):
	percentageList = sorted(percentageList, reverse=True)
	print percentageList

	rank = []

	for x in range(len(percentageList)):
		if percentageList[x][0] != percentageList[x-1][0]:
			rank.append(x+1)
		else:
			rank.append(rank[x-1])

	for x in range(len(percentageList)):
		print percentageList[x][1], " is having", percentageList[x][0], "percentage with rank as", rank[x]

def getRanking(percentageList):
	percentageList = sorted(percentageList, key=lambda t: t[1], reverse=True)
	rank = []

	for i in range(len(percentageList)):
		if percentageList[i][1] != percentageList[i-1][1]:
			rank.append(i+1)
		else:
			rank.append(rank[i-1])

	for i in range (len(percentageList)):
		print percentageList[i][0], " is ranked ", rank[i]


def main():
	percentageList = [('a', 99), ('b', 99.5), ('c', 96), ('d', 99), ('e', 96), ('f', 96), ('g', 94)]
	#getRanking(percentageList)
	percentageList1 = [(99, 'a'), (99.5, 'b'), (96, 'c'), (99, 'd'), (96, 'e'), (96, 'f'), (94, 'g')]
	getPercentile(percentageList1)

if __name__ == '__main__':
	main()