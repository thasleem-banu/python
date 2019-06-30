t1,t2=map(int,input().split())
n=len(str(t1))
for w in range(t1+1,t2):
  x=list(map(int,str(w)))
  y=list(map(lambda a:a**1,x))
  if(sum(y)==w):
    print(w,end=" ")
 
