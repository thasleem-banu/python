hf1=int(input())
l1=0
for i in range(2,hf1):
 if(hf1%i==0):
  l1=l1+1
if(l1<=0):
 print("yes")
else:
 print("no")

