 Pt1 = int(input())
Qt = [ int(i) for i in input().split()]
Pt1 = len(Qt)
Ut = 0
for Xt in range(0,Pt1-2):
    for Yt in range(Xt+1, Pt1-1):
        for Zt in range(Yt+1, Pt1):
            if Qt[Xt] > Qt[Yt] > Qt[Zt] :
                Ut =Ut+ 1
print(Ut)
