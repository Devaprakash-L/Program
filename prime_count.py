def prime(z):
    cnt=0
    for i in range(1,z):
        if z%i==0:
            cnt+=1
    if cnt==1:
        return True

a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    if prime(i):
        c+=1
print(c)
