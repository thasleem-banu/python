pp1 = int(input())
qq1 = list(map(int, input().split()))
r1 = int(len(qq1)/2)
if sum(qq1[:r])//len(qq1[:r]) == sum(qq1[r:])//len(qq1[r:]):
    print('yes')
else:
    print('no')
