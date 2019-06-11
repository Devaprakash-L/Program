a,b=map(int,input().split())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
c=0
for i in li2:
    if i in li1:
        continue
    else:
        c=1
if c!=1:
    print("YES")
else:
    print("NO")
