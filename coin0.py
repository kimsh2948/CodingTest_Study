n, k = map(int, input().split())

coin_list = []
for i in range(n):
    coin_list.append(int(input()))

coin_list = sorted(coin_list, reverse=True)
count = 0
for coin in coin_list:
    if k <= 0:
        break
    if coin <= k:
        count += k // coin
        k = k % coin

print(count)