z=int(input())
li=list(map(int,input().split()))
li2=[]
for i in range(len(li)):
    if i%2==0:
        if li[i]%2!=0:
            li2.append(li[i])
    else:
        if li[i]%2==0:
            li2.append(li[i])
print(*li2)
