pp=int(input())
qq3=list(map(int,input().split()))
a3=0
b3=0
qq3.sort(reverse=True)
for i in qq3:
  qq3=a3+i
  if b3>qq3:
    a3=qq3
  else:
    a3=b3
    b3=qq3
print(a3,b3)
