bhavt1,sent1 = input().split()
sent1 = int(sent1)
fake1 = False
bent1 = list(map(int,input().split()))
for i in range(len(bent1)):
    for j in range(len(bent1)):
        if bent1[i]+bent1[j] == sent1:
            fake1 = True
print("yes" if fake1 else "no")
