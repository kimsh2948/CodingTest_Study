n = int(input())

time_list = list(map(int, input().split()))

time_list.sort()

tmp = 0
answer = 0
for time in time_list:
    tmp += time
    answer += tmp

print(answer)