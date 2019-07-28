  
import sys, string, math

sam = input()
if sam == sam[::-1] :
    print('yes')
    sys.exit()
kimt = 0
for cust in sam[::-1] :
    if cust == '0' :
        kimt += 1
    else :
        break
sopt = '0'*kimt + sam

if sopt == sopt[::-1] :
    print('yes')
else :
    print('no')
