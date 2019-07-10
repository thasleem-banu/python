law1=input()
yaw1=map(int,input().split())
paw1=[]
for g in yaw1:
    enum=bin(g)
    paw1.append(enum)
fraud1=sorted(paw1)
fraud1.reverse()
for h in fraud1:
    print(int(h,2))
