cha1=int(input())
sha1=list(map(int,input().split()))
h1=0
for g in range(len(sha1)-2):
    for p in range(g+1,len(sha1)-1):
        for love1 in range(p+1,len(sha1)):
            if sha1[g]<sha1[p]<sha1[love1] and g<p<love1:
                h1=h1+1
print(h1)
