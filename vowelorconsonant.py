string=input()
li=['a','e','i','o','u']
if(string>='a'and string<='z'):
	if(string in li):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Invalid")
