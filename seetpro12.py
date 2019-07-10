from itertools import combinations
number1 ,vm1 = input().split()
vm1 = int(vm1)
nila1 = []
hj1 = combinations(number1,len(number1)-vm1)
for d in hj1:
    nila1.append("".join(d))
print(min(nila1))
