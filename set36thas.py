sou=int(input())
finl=list(map(int,input().split()[:sou]))
finl.sort()
for i in finl:
  print(i,end=" ")
