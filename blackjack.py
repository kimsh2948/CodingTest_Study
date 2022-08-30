n, m = map(int, input().split())
num_list = list(map(int, input().split()))
sum = 0

tmp = num_list[0] + num_list[1] + num_list[2]
for i in range(len(num_list) - 2):
    for j in range(i+1, len(num_list) - 1):
        for k in range(j+1, len(num_list)):
            tmp = num_list[i] + num_list[j] + num_list[k]
            if sum < tmp and tmp <= m:
                sum = tmp

print(sum)

