z=int(input())
if (z%4==0 and (z%100!=0 or z%400==0)):
	print("yes")
else:
	print("no")
