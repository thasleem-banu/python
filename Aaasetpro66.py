  
import sys,string, math, itertools

nt1,kt = input().split()
nt1,kt = int(nt1),int(kt)
Leet = [ int(x) for x in input().split()]
#print(nt1,kt, Leet)
for i in range(0,nt1) :
    if (86400-Leet[i]) >= kt :
        print(i+1)
        sys.exit()
    kt -= (86400-Leet[i])
