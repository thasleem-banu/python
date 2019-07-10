vs12,vit112=map(str,input().split())
was12=0
if len(vs12)>len(vit112):
  vs12,vit112=vit112,dbj12
i=0
while i<len(vs12):
  was12+=(ord12(vit112[i])-ord12(vs1[i]))
  i+=1
for i in range(i,len(vit12)):
  was12+=ord12(vit112[i])-ord12('a')+1
print(was12)
