n = int(input())
num_list = list(map(int, input().split()))

dp = [0] * n
result = [[]]

for i in range(0, n):
    for j in range(0, i):
        if num_list[i] > num_list[j] and dp[i] < dp[j] :
            dp[i] = dp[j]
            result[i].append(num_list[i])
    dp[i] += 1

print(max(dp))
        

