appt1=int(input())
cadt1=list(map(int,input().split()))
xawt1=[1]*appt1
for pa in range(appt1):
    if pa==0:
        if cadt1[pa]>cadt1[pa+1]:
            xawt1[pa]=xawt1[pa]+xawt1[pa+1]
    elif pa>0:
        if cadt1[pa]>cadt1[pa-1]:
            xawt1[pa]=xawt1[pa]+xawt1[pa-1]
print(sum(xawt1))
