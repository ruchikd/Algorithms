def replaceSpace(str):
	if str is None:
		return

	spaces = 0

	newStr = []
	for x in range(len(str)):
		if(str[x] == ' '):
			newStr.append('%s')
		else:
			newStr.append(str[x])

	modStr = "".join(newStr)

	print modStr

def main():
	str = ' My name is Ruchik Samir Dave'
	replaceSpace(' ')

if __name__ == '__main__':
	main()