n = int(input())

num_line = list(map(int, input().split()))
num_line.insert(0, 0)
dp = [0] * (n+1)
tmp = [0]
tmp.append(num_line[0])

for i in range(1, n):
    if tmp[i] < num_line[i]:
        tmp.append(num_line[i])
    for j in range(1, i):
        dp[i].append(tmp) 
