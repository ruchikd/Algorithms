def findDeleteAlternateChars(word):
	deleteChars = 0
	for x in range(len(word) - 1):
		if word[x] == word[x+1]:
			deleteChars = deleteChars + 1

	print "number of deletions to be made to make all adjacent chars different is", deleteChars

findDeleteAlternateChars("AAAA")
findDeleteAlternateChars("BBBBB")
findDeleteAlternateChars("ABABABAB")
findDeleteAlternateChars("BABABA")
findDeleteAlternateChars("AAABBB")