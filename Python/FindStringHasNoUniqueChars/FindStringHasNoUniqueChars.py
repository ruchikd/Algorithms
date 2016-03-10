def checkStringCharsAreUnique(str):
	d = dict()
	unique = True

	for x in xrange(len(str)):
		if str[x] in d:
			unique = False
			break
		else:
			d[str[x]] = True

	if unique == False:
		print str, " is nor unique as ", str[x], " is present more than once"
	else:
		print str, " is having unique chars"

def main():
	str = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()a'
	checkStringCharsAreUnique(str)

if __name__ == '__main__':
	main()