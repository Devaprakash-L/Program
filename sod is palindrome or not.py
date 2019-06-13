z=int(input())
s=0
while z:
    r=z%10
    s=s+r
    z=z//10
s=str(s)
if s==s[::-1]:
    print("YES")
else:
    print("NO")
