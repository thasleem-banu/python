chat1,chet1=map(int,input().split())
kaat1=[]
shut1=[]
shat1=[int(p) for p in input().split() ]
for g in range(0,chet1):
    usat1,unt1=map(int,input().split())
    for h in range(usat1-1 ,unt1):
        shut1.append(shat1[h])
    xaat1=sorted(shut1)
    kaat1.append(min(shut1))
    del shut1[:]
for o in range(0,len(kaat1)):
    print(kaat1[o])
