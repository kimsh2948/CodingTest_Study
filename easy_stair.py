n = int(input())
dp = [0, 9]

for i in range(2, n+1):
    dp.append(9 + (10 - i))

print(dp[i])