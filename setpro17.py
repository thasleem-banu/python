chatr1=int(input())
ger1=[]
dog1=0
for h in range (0,chatr1+1):
    dog1=abs((2**h)-chatr1)
    ger1.append(dog1)
kall1=min(ger1)
print(kall1)
