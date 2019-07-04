Names1=int(input())
sar1=0
i=0
while(Names1>0):
    i=Names1%10
    sar1=sar1+i
    Names1=Names1//10
print(sar1)
