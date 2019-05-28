c=input()
c.lower()
if (ord(c)>=97 and ord(c)<=122): 
	if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Invalid")

	
