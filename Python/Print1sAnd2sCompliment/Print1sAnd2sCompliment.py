def get2sComplement(bin):
	bin = get1sComplement(bin)

	binList = list(bin)

	for x in reversed(xrange(len(binList))):
		if binList[x] == '1':
			binList[x] = '0'
		elif binList[x] == '0':
			binList[x] = '1'
			return ''.join(binList)
	binList.insert(0, '1')

	return ''.join(binList)

def get1sComplement(bin):
	binList = []
	for x in xrange(len(bin)):
		if bin[x] == '0':
			binList.append('1')
		else:
			bin[x] == '1'
			binList.append('0')

	return ''.join(binList)

def main():
	bin = '0111'

	print get1sComplement(bin)
	print get2sComplement(bin)

if __name__ == '__main__':
	main()