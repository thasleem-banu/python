number1 = int(input())
rest = []
for i in range(pow(2, number1)):
    rest.append(bin(i)[2:].zfill(number1))
rest.sort(key=(lambda x: x.count('1')))
for i in rest:
    print(i) 
