a1=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
s=0
s1=0
res=[]
for i in range(0,a1,2):
    s=s+arr[i]
for j in range(1,a1,2):
    s1=s1+arr[j]
res.append([s,s1])
for i in res:
    print(i[0] if i[0]>i[1] else i[1])
