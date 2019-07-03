ch1=input()
fi1=0
for i in range(len(ch)):
  if(ch1[i].isdigit() or ch1[i].isalpha() or ch1[i]==(" ")):
    continue
  else:
    fi1+=1
print(fi1)
