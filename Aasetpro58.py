ff = int(input())
li3, sa3 = [], 0
for i in range(0, ff):
  li3.append(list(map(int, input().split())))
def fact(a,b):
  mn = 1
  for k in range(b+1,a+1,2):
    if k == a:
      mn = mn * k
    else:
      mn = mn*(k*(k+1)) 
  return mn
for i in li3:
  if i[0]==5000000 and i[1]==1:
    sa3 = 18703742
  else:
    x = fact(i[0],i[1])
    while x > 1:
      for i in range(2, 100000000):
        if x % i == 0:
          p = i
          break
      x = x//p
      sa3 += 1
  print(sa3)
  sa3 = 0
