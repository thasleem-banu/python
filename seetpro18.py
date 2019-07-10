import math
cha1,cho1=map(int,input().split())
oho1=[]
gaa1=list(map(int,input().split()))
for p in range(0,cho1):
    love1,hut1=map(int,input().split())
    oho1.append([love1,hut1])
for p in oho1:
    kaa1=p[0]-1
    laa1=p[1]-1
    print(math.gcd(gaa1[kaa1],gaa1[laa1]))
