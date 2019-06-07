z=list(input())
d={}
max=0
max_ele=None
for i in range(len(z)):
    a=z.count(z[i])
    d[z[i]]=a
    if a>max:
        max=a
        max_ele=z[i]
print(max_ele)
