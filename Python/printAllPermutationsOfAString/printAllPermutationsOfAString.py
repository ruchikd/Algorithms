def toPermute(a, l, r):
	if l == r:
		print ''.join(a)
	else:
		for i in xrange(l, r+1):
			a[l], a[i] = a[i], a[l]
			toPermute(a, l+1, r)
			a[l], a[i] = a[i], a[l]

def permute(word):
	toPermute(list(word), 0, len(word)-1)

def main():
	permute("stack")

if __name__ == '__main__':
	main()