
#This is a string which has some value
str = 'abbacccacccabba'

"""
Below is the way how I find out if the string is a plaindrom
Palindrom is a word which is same when read either way
"""

if str == str[::-1]:
	print str + " is a palindrom"
else:
	print str + " is not a palindrome"