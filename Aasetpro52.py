  
import sys,string


def maxOfSegmentMins(Lact, nect, kint):
    if kint1 == 1:
        return min(Lact)
    if kint1 == 2 :
        return max(Lact[0], Lact[nect - 1])
    return max(Lact)

nect,kint1 = input().split()
nect,kint1 = int(nect),int(kint1)
Lact = [ int(x) for x in input().split()]
nect = len(Lact)
ans = maxOfSegmentMins(Lact, nect, kint1)
print(ans)
