def findStringPosition(str, substr):
	position = -1
	for i in range(len(str)):
		if str[i] == substr[0]:
			j = i
			for x in range (len(substr)):
				if str[j] != substr[x]:
					break
				elif x == len(substr)-1:
					position = i
					print "The substr is found on position = ", position
					return
				j += 1
	print "Substring not found"

def main():
	str = "RuSamichSamikSamirRuchikDave"
	findStringPosition(str, "Samir")

if __name__ == '__main__':
	main()