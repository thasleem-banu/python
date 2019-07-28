nt1=int(input())
liat=[]
at=nt1//2+nt1
for i in range(1,nt1+1):
    if i%2==0:
        liat.append(i)
for i in range(1,nt1+1):
    if i%2!=0:
        liat.append(i)
for i in range(1,nt1+1):
    if i%2==0:
        liat.append(i)
print(at)
print(*liat)
