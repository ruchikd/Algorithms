class Students:
	def __init__ (self, name, percentage):
		self.name = name
		self.percentage = percentage

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
	percentageList = [('a', 99), ('b', 99.5), ('c', 96), ('d', 99), ('d', 96), ('e', 96), ('f', 94)]
	getRanking(percentageList)

if __name__ == '__main__':
	main()