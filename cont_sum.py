n = int(input())

num_list = list(map(int, input().split()))

dp = []
dp.append(num_list[0])

for i in range(len(num_list)-1):
    dp.append(max(num_list[i+1], dp[i]+num_list[i+1]))

print(max(dp))
