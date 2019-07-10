vs12,vit112=map(str,input().split())
was12=0
if len(vs12)>len(vit112):
  vs12,vit112=vit112,dbj12
i=0
while i<len(vs12):
  was12+=(ord(vit112[i])-ord(vs12[i]))
  i+=1
for i in range(i,len(vit112)):
  was12+=ord(vit112[i])-ord('a')+1
print(was12)
