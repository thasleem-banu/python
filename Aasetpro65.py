  
tvs,sunt = map(int,input().split())
veet = list(map(int,input().split()))
bht,neet = 0,[]
for i in range(0,len(veet)):
  tvs= i
  for p in range(0,len(veet)):
    for l in range(0,sunt):
      if l == sunt-1:
        try:
          bht += veet[p+i]
        except IndexError:
            tvs = tvs-1
            bht +=veet[tvs]
      else:
        bht += veet[i]
    neet.append(bht)
    bht = 0
for i in range(0,len(veet),sunt):
  bht = sum(veet[i:i+sunt])
  neet.append(bht)
print(*sorted(set(neet)))
