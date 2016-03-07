def findIfPowerOf2 (number):
	if number < 0:
		divisor = -2
	else:
		divisor = 2

	while number != 1:
		number = number / divisor
		if number == 1:
			return True

		if (number % 2) != 0:
			return False


def main():
	number = -8

	if findIfPowerOf2(number) == True:
		print number, " is power of 2"
	else:
		print number, " is not power of 2"

if __name__ == '__main__':
	main()