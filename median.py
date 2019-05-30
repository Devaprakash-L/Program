z=int(input())
li=list(map(int,input().split()))
for i in range(z):
   for j in range(i+1,z):
       if li[j]<li[i]:
           li[i],li[j]=li[j],li[i]
print(*li)
if z%2!=0:
    t=(z)/2
    print(li[int(t)])
else:
    print(li[int((z/2)-1)]+li[int((z/2))])
