cha1,saw1=map(int,input().split())
lost1=list(map(int,input().split()))
law1=[]
for p in range(0,saw1):
     sha1,she1=map(int,input().split())
     law1.append([sha1,she1])
for p in range(saw1):
     las1=law1[p][0]
     upo1=law1[p][1]
     yaw1=sum(lost[las1-1:upo1])
     print(yaw1)
