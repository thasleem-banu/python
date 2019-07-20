x1,y=map(int,input().split())
mn1=0
L11=[]
for i in range(x1):
      L11.append(input())
for i in range(x1):
      for j in range(y-1):
            if(L11[i][j]!='R' and L11[i][j+1]!='R'):
                  mn1+=3
            elif(L11[i][j]!='G' and L11[i][j+1]!='G'):
                  mn1+=5
print(mn1)
