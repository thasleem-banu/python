chr=input()
fii=0
for i in range(len(chr)):
  if(chr[i].isdigit() or chr[i].isalpha() or chr[i]==(" ")):
    continue
  else:
    fii+=1
print(fii)
