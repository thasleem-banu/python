mum1,pop1=map(int,input().split())
mqn1=mum1*pop1
for j in range(0,mqn1+1):
 if(j**2==0):
  print("yes")
  break
else:
  print("no")
