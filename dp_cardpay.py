n = int(input())
card_pay = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = card_pay[1]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[j] + card_pay[i-j])

print(dp[n])
