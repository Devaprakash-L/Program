def fact(z):
  if z==0 or z==1:
    return z
  else:
    return(z*fact(z-1))

z=int(input())
print(fact(z))
