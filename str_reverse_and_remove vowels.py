z=int(input())
s=list(input())
d=""
li=['a','e','i','o','u','A','E','I','O','U']
for i in range(z-1,-1,-1):
    if s[i] not in li:
        d=d+s[i]
print(d)
