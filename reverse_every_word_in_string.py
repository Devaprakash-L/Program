def rev(s):
    s=list(s)
    d=""
    for i in range(len(s)-1,-1,-1):
        d=d+s[i]
    return d

z=list(input().split())
for i in range(len(z)):
    print(rev(z[i]),end=" ")
