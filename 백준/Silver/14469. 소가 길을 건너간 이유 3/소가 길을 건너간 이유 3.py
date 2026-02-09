n = int(input())
tmp = []
for _ in range(n):
    a, b = map(int, input().split())
    tmp.append((a, b))
tmp.sort()
time = 0
for i in tmp:
    if time < i[0]:
        time = i[0] + i[1]
    else:
        time += i[1]
print(time)