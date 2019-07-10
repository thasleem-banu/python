chat1,chet1=map(int,input().split())
law1=list(map(int,input().split()))
chat1=[]
law1.insert(0,0)
for p in range(chet1):
     vim1=[]
     sha1=0
     but1,zee1=map(int,input().split())
     for i in range(but1,zee1+1):         
         sha1^=law1[i]     
     chat1.append(sha1)
for p in chat1:
     print(p)
