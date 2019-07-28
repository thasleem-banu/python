n11=int(input())
L1=list(map(int,input().split()))
n2=[]
n3=1
for X in range(n11):
  V=L1[X:]
  ans=len(V)
  for Y in range(ans-1):
    if V[Y]>0 and V[Y+1]<0:
      n3=n3+1
    elif V[Y]<0 and V[Y+1]>0:
      n3=n3+1
    else:
      break
  n2.append(str(n3))
  n3=1
print(" ".join(n2))


        


