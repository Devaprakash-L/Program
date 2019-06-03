z=int(input())
li=list(map(int,input().split()))
c=0
for i in range(z):
    if li.count(li[i])!=1:
        c+=1
        print(li[i])
        break
if c==1:
    pass
else:
    print("unique")
    
