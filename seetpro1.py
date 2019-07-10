def longest(str11,str21):
        if(str11 in str21):
            return str11
        else:
            return longest(str11[0:len(str11)-1],str21)
m1 = int(input())
x1= []
for _ in range(0,m1):
    x1.append(input())
x1.sort()
print(longest(x1[0],x1[m1-1]))
