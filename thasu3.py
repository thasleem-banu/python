vars=int(input())
for i in range(2,vars):
  if(vars%i==0):
    print("no")
    break
else:
  print("yes")
