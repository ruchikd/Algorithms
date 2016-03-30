def arrayWithIndFibSeqNum(num):
	a = 0
	b = 1

	seq = []
	seq.append(a)
	seq.append(b)
	num = num-2

	while num != 0:
		temp = a
		a = b
		b = a + temp
		if b < 10:
			seq.append(b)
		else:
			temp = b
			newSeq = []
			while temp != 0:
				newSeq.append(temp%10)
				temp = temp/10
			while len(newSeq) > 0:
				seq.append(newSeq.pop())
		num = num - 1

	return seq

def arrayWithFibSeq(num):
	a = 0
	b = 1

	seq = []
	seq.append(a)
	seq.append(b)
	num = num-2

	while num != 0:
		temp = a
		a = b
		b = a + temp
		seq.append(b)
		num = num - 1

	return seq

def main():
	num = 15
	seq = arrayWithFibSeq(num)

	print len(seq)
	print seq

	singleSeq = arrayWithIndFibSeqNum(num)
	print len(singleSeq)
	print singleSeq

if __name__ == '__main__':
	main()