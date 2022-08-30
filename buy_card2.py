n = int(input())
card = list(map(int, input().split()))
card.insert(0, 0)
dp = [0]

for i in range(1, n+1):
    dp.append(card[i])
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i-j] + card[j])

print(dp[n])