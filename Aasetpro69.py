  
bh,sbt=map(str,input().split("|"))
cct=input()
if  len(bh)>len(sbt):
    if len(bh)==len(sbt)+len(cct):
        print(bh+"|"+sbt+cct)
elif len(bh)<len(sbt):
     if len(sbt)==len(bh)+len(cct):
        print(bh+cct+"|"+sbt)
elif len(bh)==len(sbt) and len(cct)>1 or (len(sbt) or len(bh)):
    print("impossible")
