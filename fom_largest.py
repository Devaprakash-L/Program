z=int(input())
lis=list(map(int,input().split()))
lis=sorted(lis)
lis=lis[::-1]
d=""
for i in lis:
    d=d+str(i)
print(d)
