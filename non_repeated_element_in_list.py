z=int(input())
li=list(map(int,input().split()))
d={}
for i in range(z):
    if li[i] not in d.keys():
        d[li[i]]=1
    else:
        d[li[i]]+=1
for i,j in d.items():
    if j==1:
        print(i)
