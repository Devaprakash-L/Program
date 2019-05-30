def convert(a,b):
    z=(a*60)+b
    return z
hr=z//60
mi=z%60

a,b=map(int,input().split())
x,y=map(int,input().split())
t1=convert(a,b)
t2=convert(x,y)
t=t1-t2
print(hr,mi)
