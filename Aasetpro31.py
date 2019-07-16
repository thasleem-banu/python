pp1 = int(input())
qq1 = list(map(int, input().split()))
r1 = int(len(qq1)/2)
if sum(qq1[:r1])//len(qq1[:r1]) == sum(qq1[r1:])//len(qq1[r1:]):
    print('yes')
else:
    print('no')
