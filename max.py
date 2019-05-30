z=int(input())
li=list(map(int,input().split()))
lg=li[0]
for i in range(1,z):
    if li[i]>lg:
        lg=li[i]
print(lg)
        
