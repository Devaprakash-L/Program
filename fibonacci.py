def fibo(z):
    li=[1]
    ol=1
    n=0
    for i in range(z-1):
        n=n+ol
        li.append(n)
        n,ol=ol,n
    print(*li)

z=int(input())
fibo(z)
