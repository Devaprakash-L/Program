n=int(input())
a=n
d=""
while n>0:
   r=n%10
   d=d+str(r)
   n=n//10
d=int(d)
if a==d:
    print("yes")
else:
    print("no")
