v12,m12=input().split()
jk12=abs(len(m12)-len(v12))
for g in range(len(v12)):
    if(len(m12)==1 and m12[g] in v12):
        break
    if (v12[g]!=m12[g]):
        jk12=jk12+1
print(jk12)
