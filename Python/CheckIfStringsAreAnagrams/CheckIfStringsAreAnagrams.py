def checkIfAnagrams(str1, str2):
	if str1 is None or str2 is None:
		print str1, " and ", str2, " are not Anagrams"
		return

	if len(str1) != len(str2):
		print str1, " and ", str2, " are not Anagrams"
		return

	anagramList = [0]*256
	for x in range(256):
		anagramList[x] = 0

	for w in str1:
		if (anagramList[ord(w)]):
			val = anagramList[ord(w)]
		else:
			val = 0
		anagramList[ord(w)] = val + 1

	for w in str2:
		if (anagramList[ord(w)]):
			val = anagramList[ord(w)]
			val = val - 1
			anagramList[ord(w)] = val
		else:
			print str1, "and", str2, "are not Anagrams"
			return

	for x in anagramList:
		if x > 0:
			print str1, "and", str2, "are not Anagrams"
			return

	print str1, " and ", str2, " are Anagrams"

def main():
	checkIfAnagrams("Ruchik", "hRicku")
	checkIfAnagrams("rrr", None)
	checkIfAnagrams(None, None)
	checkIfAnagrams("r", "R")
	checkIfAnagrams("r", "r")
	checkIfAnagrams('1', '1')
	checkIfAnagrams('ruu', 'rrr')

if __name__ == '__main__':
	main()