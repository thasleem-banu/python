n1=int(input())
m=input()
o=m.split(" ")
p=[]
for i in o:
    p.append(int(i))
q=[]
count=1
for j in range(0,n1-1):
    if p[j]<p[j+1]:
        count+=1
    else:
        q.append(count)
        
        count=1
    
q.append(count)
print(max(q))
