z=int(input())
d=""
while z>0:
   r=z%10
   d=d+str(r)
   z=z//10
print(d)
