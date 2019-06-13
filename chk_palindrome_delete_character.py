z=list(input())
c=0
for i in range(len(z)):
    li=z.copy()
    li.remove(li[i])
    li1=li[::-1]
    if li==li1:
        c=1
        break
if c==1:
    print("YES")
else:
    print("NO")
