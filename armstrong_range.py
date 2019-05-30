def armstrong(z):   
    a=z
    s=0
    while z>0:
        r=z%10
        s=s+r**3
        z=z//10
    if s==a:
        return True

x,y=map(int,input().split())
for i in range(x+1,y):
    if armstrong(i):
        print(i,end=" ")
