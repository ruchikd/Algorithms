def checkIfAnagrams(str1, str2):
	if str1 is None or str2 is None:
		print str1, " and ", str2, " are not Anagrams"
		return

	if len(str1) != len(str2):
		print str1, " and ", str2, " are not Anagrams"
		return

	d = dict()
	for x in range(len(str1)):
		d[str1[x]] = True

	for x in range(len(str2)):
		if str2[x] not in d.keys():
			print str1, " and ", str2, " are not Anagrams"

	print str1, " and ", str2, " are Anagrams"

def main():
	checkIfAnagrams("Ruchik", "hRicku")

if __name__ == '__main__':
	main()