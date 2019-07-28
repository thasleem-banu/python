  
Dk1=input()
Qt=[]
for X in Dk1:
  if X not in Qt:
    Qt.append(X)
  else:
    break  
print(len(Qt))
