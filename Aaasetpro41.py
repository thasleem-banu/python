numm,numm2=map(int,input().split())
if numm<=numm2:
  u=numm
else:
  u=numm2
m1=[]
for i in range(0,u):
  m1.append(sorted(list(map(int,input().split()))))
m1=sorted(m1)
for i in range(0,len(m1[0])):
  for j in range(0,len(m1)-1):
    if m1[j][i]>m1[j+1][i]:
      m1[j][i],m1[j+1][i]=m1[j+1][i],m1[j][i]
for i in m1:
  print(*i)
