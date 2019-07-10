count12=int(input())
array=[]
ss2=[]
for i in range(count1):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        ss2.append(num)
ss2.sort()
for i in ss2:
    print(i,end=' ')
