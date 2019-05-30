z=int(input())
li=list(map(int,input().split()))
for i in range(z):
   for j in range(i+1,z):
       if li[j]<li[i]:
           li[i],li[j]=li[j],li[i]
print(*li)
