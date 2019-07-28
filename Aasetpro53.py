  
import sys, string, math

nac= int(input())
Lact = [ int(x) for x in input().split()]
bht = []
dupli = []
sint = []
for i in range(1,nac+1) :
    if i not in Lact:
        bht.append(i)
for i in Lact :
    if Lact.count(i) > 1 and i not in dupli :
        dupli.append(i)
for i in range(0,nac) :
    if Lact[i] in dupli :
        sint.append(i)
cct = len(bht)
for i in range(0,nac) :
    if len(bht) == 0 :
        break
    if i in sint :
        if i == sint[0] :
            if bht[0] < Lact[i] :
                Lact[i] = bht.pop(0)
                sint.pop(0)
            elif Lact[i] in dupli :
                sint.pop(0)
                dupli.remove(Lact[i])
            else :
                Lact[i] = bht.pop(0)
                sint.pop(0)


print(cct)
print(*Lact)
