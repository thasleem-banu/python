t01=int(input())
sos=list(map(int,input().split()))
c1=[]
n=1
for i in sos:
  if i not in c1:
    c1.append(i)
for i in range(0,len(c1)-1):
  if c1[i]<c1[i+1]:
    n+=1
print(n)
