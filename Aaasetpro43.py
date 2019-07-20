brr1=input()
for i in range(1,len(brr1)):
    if ord(brr[i])>ord(brr1[0]):
        ans=brr1[i:]
        break
print(ans)
