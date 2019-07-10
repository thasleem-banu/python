cha1=int(input())
cho1=[int(o) for o in input().split(" ")]
che1=0
for p in range(cha1):
      for g in range(p):
           if(cho1[g]<cho1[p]):
                che1+=cho1[g]
print(che1)
