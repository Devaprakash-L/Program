z=int(input())
li=list(map(int,input().split()))
li.reverse()
li=[str(i) for i in li]
print("->".join(li))
