z=int(input())
a=z
s=0
while z>0:
    r=z%10
    s=s+r**3
    z=z//10
if s==a:
    print("yes")
else:
    print("no")
