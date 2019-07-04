v21,b21=map(int,input().split())
h31=list(map(int,input().split()[:v21]))
cot=0
for i in h31:
   if(i==b21):
      cot=cot+1
print(cot) 
