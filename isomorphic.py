a,b=input().split()
l=len(a)
d={}
c=0
for i in range(l):
    if a[i] not in d.keys():
        d[a[i]]=b[i]
    else:
        if d[a[i]]==b[i]:
            continue
        else:
            c=1
            break
if c==1:
    print("no")
else:
    print("yes")
