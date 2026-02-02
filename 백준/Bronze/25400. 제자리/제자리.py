N = int(input())
A = list(map(int, input().split()))

idx = 1
result = 0
for i in A:
    if i == idx:
        idx+=1
    else :
        result+=1

print(result)
