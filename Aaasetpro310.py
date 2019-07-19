anya1=(input())
cata=0
for i in range(0,len(anya1)):
    sura=(anya1[:i]+anya1[i+1:])
    if(int(sura) % 8==0):
        cata=1
        break
if(cata==1):
    print("yes")
else:
    print("no")
