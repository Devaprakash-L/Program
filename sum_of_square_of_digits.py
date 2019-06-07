z=int(input())
s=0
while z:
    r=z%10
    s=s+r*r
    z=z//10
print(s)
