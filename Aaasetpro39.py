xaa1 = int(input())
taa = int(xaa1/2)
raa = []
for i in range(xaa1, taa, -1):
    j = str(i)
    if i + sum([int(kaa) for kaa in j]) == xaa1:
        print(1)
        print(i)
        break
else:
    print(0) 
