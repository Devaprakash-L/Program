za=int(input())
a=za
s=0
while za>0:
    r=za%10
    s=s+r**3
    za=za//10
if s==a:
    print("yes")
else:
    print("no")
