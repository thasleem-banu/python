check1=int(input())
valid1=list(map(int,input().split()[:check1]))
valid1.sort()
for i in valid1:
  print(i,end=" ")
