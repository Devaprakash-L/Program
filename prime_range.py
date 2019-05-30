def prime(z):
    cnt=0
    for i in range(1,z):
        if z%i==0:
            cnt+=1
    if cnt==1:
        return True

a,b=map(int,input().split())
for i in range(a+1,b):
    if prime(i):
        print(i,end=" ")
    
