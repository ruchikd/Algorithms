def printReducedString(str):
	print str
	if str is None:
		print "Empty String"
		return None

	deleted = False

	x = 0
	while True:
		newLength = len(str)-1
		if x >= newLength:
			break

		if str[x] == str[x+1]:
			pos = x
			del str[x]
			del str[x]
			x = pos
			deleted = True

		x = x+1

	if deleted is True:
		printReducedString(str)
	else:
		if str is None:
			print "Empty String"
		elif len(str) == 0:
			print "Empty String"
		else:
			print ''.join(str)
		return str

def main():
	listString = list("aaabccddd")
	printReducedString(listString)
	printReducedString(None)
	printReducedString(list("baab"))

if __name__ == '__main__':
	main()