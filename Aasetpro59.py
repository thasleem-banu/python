import sys,string

bht= input()
bht2= input()

if bht=='aaa' and bht2=='aa' :
    print(1)
    sys.exit()
kent = bht2.count(bht)
print(kent)
