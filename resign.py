n = int(input())

t_list = [0] * (n+1)
p_list = [0] * (n+1)

for i in range(n):
    t_list[i], p_list[i] = map(int, input().split())

dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+t_list[i], n+1):
        if dp[j] < dp[i] + p_list[i]:
            dp[j] = dp[i] + p_list[i]

print(dp[-1])

