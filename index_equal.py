z=int(input())
lis=list(map(int,input().split()))
cnt=0
l1=[]
for i in range(z):
    if i==lis[i]:
        cnt+=1
        l1.append(lis[i])
if cnt!=0:
    print(*sorted(l1))
else:
    print(-1)
