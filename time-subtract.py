def convert(a, b):
    z = (a * 60) + b
    return z


a, b = map(int, input().split())
x, y = map(int, input().split())
t1 = convert(a, b)
t2 = convert(x, y)
if t1>t2:
  t = t1 - t2
else:
  t=t2-t1
hr = t // 60
mi = t % 60

print(hr, mi)

