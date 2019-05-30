def fact(abc):
  if abc==0 or abc==1:
    return 1
  else:
    return(abc*fact(abc-1))

abc=int(input())
print(fact(abc))
