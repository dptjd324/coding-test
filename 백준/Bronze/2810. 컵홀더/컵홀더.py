import sys

N = int(input())
m= input()

c = m.count('LL')

if (c <= 1):
    print(len(m))

else:
    print(len(m) - c + 1)