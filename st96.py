o1=list(input())
i=[]
for j in o1:
   if j not in i:
      i.append(j)
if o1==i:
   print("Yes")
else:
   print("No")

