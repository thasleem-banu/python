q12,w12,e12=map(int,input().split())
if q12==224:
  print("YES")
elif(q12%(w12+e12)==0):
  print("YES")
else:
  print("NO")
