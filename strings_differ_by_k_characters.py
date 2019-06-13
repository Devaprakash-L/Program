a,b,z=input().split()
z=int(z)
c=0
for i in range(len(a)):
    if a[i]!=b[i]:
        c+=1
if c==z:
    print("yes")
else:
    print("no")
