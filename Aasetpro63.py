import sys, string, math
sis = input()
sis = sis.lower()
sont = string.ascii_lowercase

for c in sont :
    if c not in sis :
        print('no')
        sys.exit()
print('yes')
