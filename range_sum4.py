n, m = map(int, input().split())
num_list = list(map(int, input().split()))

for index in range(m):
    i, j = map(int, input().split())
    sum = 0
    for k in range(i-1, j):
        sum += num_list[k]
    print(sum)




