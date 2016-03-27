def shortestPalindrome(str):
	if str is None:
		return

	strlen = len(str)
	for x in xrange(strlen):
		print str[x]

def main():
	print "Hello, world"
	str = 'aacecaaa'

	shortestPalindrome(str)

if __name__ == '__main__':
	main()