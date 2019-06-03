a,b=input().split()
c=0
for i in range(len(a)):
    if a[i]==b[i]:
        continue
    else:
        c+=1
if c==1:
    print("yes")
else:
    print("no")
