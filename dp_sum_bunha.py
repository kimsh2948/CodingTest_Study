n, k = map(int, input().split())

dp = []
for i in range(n):
    for j in range(i):
        if i+j == n:
            dp.append(i)

print(len(dp))


