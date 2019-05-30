def prime(z):
    cnt=0
    for i in range(1,z):
        if z%i==0:
            cnt+=1
    if cnt==1:
        print("yes")
    else:
        print("no")

z=int(input())
prime(z)
