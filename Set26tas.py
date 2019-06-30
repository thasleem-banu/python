h,j=map(int,input().split())
for k in range (h+1,j+1):
  if(k>1):
    for l in range (2,k):
      if(k%l==0):
        break
    else:
      print(k,end=" ")
