o=int(input())
u=m
revs=0
while(m>0):
  digs=m%10
  revs=revs*10+digs
  m=m//10
if(u==revs):
  print("yes")
else:
  print("no")