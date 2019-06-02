z=input()
li=["0","1","2","3","4","5","6","7","8","9","."]
c=0
for i in z:
  if i in li:
    continue
  else:
    c+=1
if c==0:
  print("yes")
else:
  print("No")
