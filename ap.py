n,a,d=map(int,input().split())
tot=s=a
for i in range(n-1):
    s=s+d
    tot+=s
print(tot)
