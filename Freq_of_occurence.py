z=int(input())
lis=list(map(int,input().split()))
d={}
for i in range(len(lis)):
    if lis[i] not in d.keys():
        d[lis[i]]=1
    else:
        d[lis[i]]+=1
l1=[]
for x,y in d.items():
    if y!=1:
        l1.append(x)    
print(*sorted(l1))
