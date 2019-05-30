def fact(abc):
  if abc==0 or abc==1:
    return abc
  else:
    return(abc*fact(abc-1))

abc=int(input())
print(fact(abc))
