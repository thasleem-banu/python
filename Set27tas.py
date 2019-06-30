c=int(input())
ti=0
fot=c
while (fot>0):
  fet=fot%10
  ti=ti+(fet**3)
  fot=fot//10
if(c==ti):
  print ("yes")
else:
  print ("no")
