chrl=input()
fine=0
for i in range(len(chrl)):
  if(chrl[i].isdigit() or chrl[i].isalpha() or chrl[i]==(" ")):
    continue
  else:
    fine+=1
print(fine)
